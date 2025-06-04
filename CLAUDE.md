# Backend Guidelines

## 🚀 BREAKTHROUGH DISCOVERY: Apple JSON API Endpoints!

**Game-Changing Finding**: Apple provides JSON API endpoints for ALL documentation pages! No HTML scraping or browser automation needed.

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

## Project Mission
Create a comprehensive Python scraper to mirror Apple's entire developer documentation ecosystem (150+ frameworks, 100,000+ pages) for Context7 integration, enabling natural language queries like "apple swiftui" or "apple metal" to retrieve accurate, up-to-date documentation.

## Claude Guidelines

### Critical Rules - DO NOT VIOLATE

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

3. **Phased Rollout** 🚀 READY!
   - **READY**: SwiftUI pilot (~1,500 pages in ~5 minutes)
   - **Next**: Core frameworks (UIKit, Foundation, Swift)
   - **Future**: Complete all 150+ frameworks (~3 hours total)
   - ✅ Hash-based incremental update system ready

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
