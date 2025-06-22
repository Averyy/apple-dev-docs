# Apple Developer Documentation Scraper - Project Context

## Project Overview
Building a comprehensive Python scraper to mirror Apple's entire developer documentation ecosystem with local MCP server integration. This enables developers to use natural language queries to retrieve accurate, up-to-date Apple developer documentation.

## Scale & Scope
- **Frameworks**: 341 frameworks across all Apple platforms ✅ COMPLETE
- **Documents**: 341,207 documentation pages ✅ COMPLETE
- **Embeddings**: 323,118 vectors indexed in ChromaDB
- **Platforms**: iOS, macOS, tvOS, watchOS, visionOS, Catalyst
- **Cost**: ~$5.00 USD for initial embedding generation

## Technical Architecture

### Core Technologies
- **Language**: Python 3.11+ with type hints
- **Scraping**: httpx (Apple JSON API), async concurrency
- **API**: Apple's internal JSON endpoints (`/tutorials/data/documentation/`)
- **Optimization**: ETag-based change detection for efficient updates
- **Storage**: Local filesystem with SHA-256 hash deduplication

### Repository Structure
```
apple-developer-docs/
├── README.md
├── context7.json           # Context7 configuration
├── .hashes/                # Content tracking
├── SwiftUI/                # Framework folders
├── UIKit/
├── Foundation/
├── [... all frameworks]
└── _metadata/              # Scraping progress & indexes
```

## Implementation Status

### Phase 1: SwiftUI Pilot ✅ COMPLETE
- ✅ Scraped ~1,500 SwiftUI pages successfully
- ✅ Validated markdown quality and structure
- ✅ Refined scraping patterns and error handling

### Phase 2: Core Frameworks ✅ COMPLETE
- ✅ Added UIKit, Foundation, Swift Standard Library
- ✅ Implemented cross-framework linking
- ✅ Optimized hash system with ETag support

### Phase 3: Full Coverage ✅ COMPLETE
- ✅ Scraped all 341 frameworks systematically
- ✅ Implemented parallel scraping (10 concurrent connections)
- ✅ Deployed incremental update system with ETag optimization

### Current Status: Production Deployed ✅
- **Total documents**: 341,207 pages across 341 frameworks
- **Vector index**: 323,118 embeddings in ChromaDB
- **MCP Server**: Deployed at http://192.168.2.5:8080/mcp/
- **Search performance**: <500ms with platform filtering
- **Auto-updates**: Weekly via Docker cron job

## Key Requirements

### Content Quality
- Preserve exact Apple documentation structure
- Maintain all code examples with proper syntax highlighting
- Extract complete metadata (availability, deprecation, beta status)
- Generate clean, semantic markdown

### Technical Standards
- Efficient change detection via content hashing
- Graceful error handling and retry logic
- Respect rate limits (delays between requests)
- Comprehensive logging for debugging

### Markdown Format
Each page follows a consistent template:
```markdown
# [Component Name]

**Framework**: [Framework]  
**Availability**: iOS 15.0+, macOS 12.0+, ...  
**Import**: `import [Framework]`

[Description]

## Declaration
```swift
[Full declaration]
```

## Code Examples
[Practical examples]

## Related APIs
[Cross-references]
```

## Context7 Integration

### Search Optimization
- Framework aliases ("apple swiftui" → SwiftUI docs)
- Common query patterns
- Cross-framework navigation

### Configuration
```json
{
  "projectTitle": "Apple Developer Documentation",
  "description": "Complete official Apple documentation...",
  "rules": [
    "Check platform availability before using APIs",
    "Prefer modern Swift concurrency patterns",
    ...
  ]
}
```

## Success Metrics ✅ ALL ACHIEVED
- ✅ All 341 frameworks indexed
- ✅ 341,207 pages with proper formatting
- ✅ Working cross-references between frameworks
- ✅ Efficient incremental updates via ETag optimization
- ✅ MCP server deployed and operational
- ✅ ChromaDB vector search with <500ms response time
- ✅ Platform-aware filtering (iOS, macOS, tvOS, etc.)

## Current Status: COMPLETE & PUBLIC READY
- ✅ Scraping infrastructure complete
- ✅ All Apple documentation successfully indexed
- ✅ MCP server deployed with Docker
- ✅ 100% test coverage passing
- ✅ Ready for public GitHub release