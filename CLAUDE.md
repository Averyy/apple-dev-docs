# Backend Guidelines

## Apple JSON API Endpoints!

Apple provides JSON API endpoints for ALL documentation pages! No HTML scraping or browser automation needed.

### JSON Endpoint Pattern:
```
Documentation URL: https://developer.apple.com/documentation/swiftui/text
JSON API URL:      https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
```

### Why This Changes Everything:
- ✅ **No JavaScript rendering needed** - Direct HTTP requests to JSON endpoints
- ✅ **100x faster** - No browser automation, just pure API calls
- ✅ **Complete data** - All content, code examples, metadata in structured format
- ✅ **Scalable to 100,000+ pages** - Simple async HTTP requests
- ✅ **Generic solution** - One scraper works for ALL frameworks
- ✅ **ETag Support** - Apple's API provides ETags for efficient change detection!

### ETag-Based Change Detection
Apple's JSON API supports HTTP ETags, enabling efficient incremental updates:
```bash
# First request returns ETag header
curl -I https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
# ETag: W/"399a0f24205d58c9443159732da8989a"

# Subsequent requests can check if content changed
curl -H 'If-None-Match: W/"399a0f24205d58c9443159732da8989a"' ...
# Returns 304 Not Modified if unchanged, or 200 with new content if updated
```

This means after initial scraping with ETag collection, we can check all 278K documents for changes efficiently using just HEAD requests!

### Actual Project Size (Production Data):
- **Documentation files**: 278,778 files (1.17GB total on disk)
- **ETag storage**: Single JSON file - easily fits in GitHub
- **Vectorstore size**: ~1.1GB (OpenAI 1536 dimensions)
- **Initial embeddings cost**: $3.74 (OpenAI text-embedding-3-small)

### ETag Storage Strategy:
Using a single `/data/metadata/etags.json` file containing all ETags:
- Manageable size (~10MB for 45K entries)
- Fast O(1) lookups when loaded into memory
- Atomic updates for transactional consistency
- Simple backup/restore operations
- Matches existing single-file patterns (frameworks list, progress tracking)

## Project Mission
Create a comprehensive Python scraper to mirror Apple's entire developer documentation ecosystem (340+ frameworks, 278,778 pages) with local MCP server integration, enabling natural language queries to retrieve accurate, up-to-date Apple developer documentation.

## Claude Guidelines

### Critical Rules - DO NOT VIOLATE

## Comprehensive Coverage Analysis

### Current Implementation Strengths:
1. ✅ **New framework added to technologies.json** - Handled by fetching fresh list each run
2. ✅ **Existing page content updated** - Handled via ETag + hash comparison
3. ✅ **New sub-page added deep in hierarchy** - Handled via iterative discovery
4. ✅ **Framework main page unchanged but children update** - Handled by always discovering child pages
5. ✅ **Circular references** - Handled via `processed_urls` set
6. ✅ **ETags for efficient change detection** - Fully implemented

### Identified Gaps:

#### 1. **New page added to existing framework** ⚠️
- **Issue**: Only pages referenced in existing JSON files are discovered
- **Gap**: Hidden or newly added pages not linked from existing pages won't be found
- **Fix**: Need periodic full re-discovery or monitoring of framework changes

#### 2. **Page removed/deprecated** ❌ 
- **Issue**: No mechanism to detect and clean up removed pages
- **Gap**: Orphaned markdown files remain in documentation folder
- **Fix**: Need to track all scraped files and compare with current discovery

#### 3. **Cross-framework references** ⚠️
- **Issue**: Currently filtered out (only same-framework refs processed)
- **Gap**: Cross-framework links become broken in local documentation
- **Fix**: Option to include cross-framework refs or convert to Apple URLs

#### 4. **Hidden/unlisted pages** ❌
- **Issue**: Only JSON-referenced pages are discovered
- **Gap**: Direct-access pages without references are missed
- **Fix**: Need URL pattern scanning or sitemap.xml if available

#### 5. **Race conditions** ✅
- **Non-issue**: Single-threaded per framework prevents races
- **Note**: Multiple frameworks can run concurrently safely

#### 6. **Incremental framework detection** ⚠️
- **Issue**: Always fetches all frameworks, no change detection
- **Gap**: Can't detect when framework list itself changes
- **Fix**: Store and compare technologies.json ETag

### Recommended Fixes:

1. **Orphan Detection System**:
   ```python
   # After discovery, compare with existing files
   existing_files = set(glob(f"{output_dir}/**/*.md"))
   current_urls = set(discovered_urls)
   orphaned = existing_files - current_urls
   ```

2. **Full Re-discovery Mode**:
   ```python
   # Add --full-rediscovery flag to ignore ETags for discovery
   # Useful for finding new unreferenced pages
   ```

3. **Cross-Framework Reference Handling**:
   ```python
   # Add config option for cross-framework handling
   # Either: include refs, convert to URLs, or create stub pages
   ```

4. **URL Pattern Discovery**:
   ```python
   # Probe common patterns like:
   # /documentation/{framework}/getting-started
   # /documentation/{framework}/release-notes
   ```

- **NEVER create mock data or simplified components** unless explicitly told to do so
- **NEVER replace existing complex components with simplified versions** - always fix the actual problem
- **ALWAYS work with the existing codebase** - do not create new simplified alternatives
- **ALWAYS find and fix the root cause** of issues instead of creating workarounds
- When debugging issues, focus on fixing the existing implementation, not replacing it
- When something doesn't work, debug and fix it - don't start over with a simple version
- If anything is unclear or you're not sure - ask
- **NEVER** impersonate people and team members, do the role you are assigned and don't reply as if you're someone else

### Python Development Standards

- Use Python 3.11+ with type hints for all functions
- Follow PEP 8 style guidelines
- Use `asyncio` for concurrent operations
- Always validate scraped data before processing
- Use proper logging (not print statements)
- Run `mypy` for type checking before considering code complete
- Optimize for performance (0.2s rate limits, 10 concurrent requests)
- Design for memory efficiency with URL cache cleanup
- Design for multiple concurrent users from day one

### Scraping Ethics & Best Practices

- Add delays between requests
- Use random User-Agent headers
- Cache responses when appropriate to minimize server load
- Log all scraping activities for debugging

### Data Storage Principles

- Store markdown documents locally in documentation/ folder mirroring Apple's hierarchy
- Use SHA-256 hashing for content deduplication and change detection
- Preserve framework structure in directory organization
- Track scraping progress and metadata separately

### Security & API Key Management

**CRITICAL: API Key Security**
- ✅ **Environment Variables Only**: All API keys must be stored in environment variables
- ❌ **Never Hardcode**: API keys must never appear in source code
- ✅ **Environment File**: Use `.env` file (which is gitignored) for local development
- ✅ **Model Restrictions**: OpenAI API key is restricted to `text-embedding-3-small` only
- ✅ **Error Handling**: Scripts must validate API key presence before execution

**Example Secure Configuration:**
```python
import os

# CORRECT: Use environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable must be set")

# WRONG: Never do this
# api_key = "sk-1234567890abcdef"  # ❌ NEVER HARDCODE
```

## Project Architecture

### Core Components (Updated for JSON API)

1. **Generic JSON Scraper**: Single scraper that works for ALL Apple frameworks
2. **URL Discovery**: Traverse JSON references to find all documentation pages
3. **JSON to Markdown Converter**: Transform structured JSON to clean markdown
4. **Hash Manager**: Track changes and avoid duplicate scraping
5. **Progress Tracker**: Monitor completion across 150+ frameworks

### Key Technologies (Simplified!)

- **Web Scraping**: httpx (async HTTP client) - that's it!
- **JSON Processing**: Built-in json module
- **Storage**: Local filesystem only (MVP)
- **Deployment**: Docker, with environment-based configuration
- **NO LONGER NEEDED**: BeautifulSoup4, markdownify, pyppeteer

## Development Workflow

1. **Research Phase** ✅ COMPLETE!
   - JSON API discovered at `/tutorials/data/documentation/`
   - All content available in structured JSON format
   - No HTML parsing needed
   - Framework hierarchy preserved in JSON references

2. **Implementation** ✅ COMPLETE!
   - ✅ Generic JSON scraper implemented for ALL frameworks
   - ✅ URL transformation and link fixing completed
   - ✅ Optimized async HTTP (0.2s delays, 10 concurrent)
   - ✅ JSON to Markdown conversion with proper formatting
   - ✅ Memory management and error handling implemented
   - ✅ ETag-based optimization for efficient incremental updates

3. **Production Deployment** ✅ COMPLETE!
   - ✅ All 341 frameworks scraped (278,778 pages total)
   - ✅ ETag collection complete for efficient updates
   - ✅ Hash-based incremental update system operational
   - ✅ Comprehensive test coverage for critical functionality
   - ✅ Production scripts cleaned and optimized

## Code Quality Checklist

Before committing code:

- Type hints added to all functions
- Docstrings for all classes and public methods
- Error handling for network requests
- Logging instead of print statements
- No hardcoded values or credentials
- Tests written for new functionality
- Markdown output manually reviewed
- Source URLs preserved for all content
- Platform availability metadata accurate
- Cross-framework references validated
- Context7 configuration tested

## Apple Documentation Structure

### Framework Categories
- **UI Frameworks**: SwiftUI, UIKit, AppKit
- **Graphics & Games**: Metal, SceneKit, SpriteKit, RealityKit
- **Media**: AVFoundation, Core Audio, Vision
- **App Services**: CloudKit, Core Data, StoreKit
- **System**: Foundation, Security, Network
- **ML/AI**: Core ML, Natural Language, Create ML
- **AR/VR**: ARKit, RoomPlan, visionOS frameworks
- **Health**: HealthKit, CareKit, ResearchKit

### Output Format Example
```markdown
# [API Name]

**Framework**: [Framework]  
**Availability**: iOS 15.0+, macOS 12.0+, ...  
**Import**: `import [Framework]`

[Description]

## Declaration
```swift
[Full Swift declaration]
```

## Code Examples
[Practical examples with syntax highlighting]

## See Also
- [Related APIs with proper linking]
```

## Context7 Integration Goals

- Enable queries like "apple swiftui list", "apple metal shader"
- Maintain framework aliases for natural language search
- Preserve all code examples with proper formatting
- Support cross-framework navigation
- Provide platform-specific guidance
