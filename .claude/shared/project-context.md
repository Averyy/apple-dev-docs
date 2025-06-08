# Apple Developer Documentation Scraper - Project Context

## Project Overview
Building a comprehensive Python scraper to mirror Apple's entire developer documentation ecosystem with local MCP server integration. This enables developers to use natural language queries to retrieve accurate, up-to-date Apple developer documentation.

## Scale & Scope
- **Target**: 341 frameworks across all Apple platforms ✅ COMPLETE
- **Actual Pages**: 278,778 documentation pages (1.17 GB) ✅ COMPLETE
- **Platforms**: iOS, macOS, tvOS, watchOS, visionOS
- **Frameworks**: SwiftUI, UIKit, Metal, ARKit, Core ML, HealthKit, and 300+ more

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

### Current Status: Production Ready
- **Total scraped**: 278,778 pages across 341 frameworks
- **ETag collection**: Complete for efficient incremental updates
- **Test coverage**: Comprehensive critical path testing
- **Performance**: ~300 pages/minute with change detection

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

## Success Metrics ✅ ACHIEVED
- ✅ All 341 frameworks indexed (exceeded target)
- ✅ 278,778 pages with proper formatting (far exceeded target)
- ✅ Working cross-references between frameworks
- ✅ Efficient incremental updates via ETag optimization
- 🚧 Context7/MCP integration (next phase)

## Current Status: Ready for MCP Integration
- ✅ Scraping infrastructure complete and production-ready
- ✅ All Apple documentation successfully mirrored
- ✅ Comprehensive test coverage for critical functionality
- 🚧 Moving to Task 2: Vector Index Building for MCP server