# Apple Developer Documentation Scraper - Project Context

## Project Overview
Building a comprehensive Python scraper to mirror Apple's entire developer documentation ecosystem with local MCP server integration. This enables developers to use natural language queries to retrieve accurate, up-to-date Apple developer documentation.

## Scale & Scope
- **Frameworks**: 373 frameworks across all Apple platforms (as of December 2025)
- **Documents**: 334,468 documentation pages
- **Search Engine**: Meilisearch for ultra-fast full-text search
- **Platforms**: iOS, macOS, tvOS, watchOS, visionOS, Catalyst
- **Last Update**: December 21, 2025 (includes WWDC 2025 updates)

## Technical Architecture

### Core Technologies
- **Language**: Python 3.11+ with type hints
- **Scraping**: httpx (Apple JSON API), async concurrency
- **API**: Apple's internal JSON endpoints (`/tutorials/data/documentation/`)
- **Search**: Meilisearch for sub-500ms search with platform filtering
- **Optimization**: ETag-based change detection for efficient updates
- **Storage**: Local filesystem with SHA-256 hash deduplication

### Repository Structure
```
apple-dev-docs/
├── README.md
├── CLAUDE.md               # Development guidelines
├── context7.json           # Context7 configuration
├── scrape.py               # Main documentation scraper
├── .hashes/                # Content tracking
├── documentation/          # Scraped markdown files
│   ├── SwiftUI/
│   ├── UIKit/
│   ├── Foundation/
│   └── [... 370+ frameworks]
├── meilisearch/            # Meilisearch data (Docker volume)
├── scripts/                # Utility scripts
│   └── index_to_meilisearch.py
└── mcp-server/             # MCP server implementation
    ├── apple_docs_stdio_mcp.py    # STDIO MCP server
    ├── apple_docs_remote_client.py # Remote client bridge
    ├── meilisearch_adapter.py     # Meilisearch integration
    ├── http_stdio_wrapper.py      # HTTP wrapper for Docker
    └── tests/                     # Test suite
```

## Implementation Status

### Phase 1: SwiftUI Pilot - COMPLETE
- Scraped ~1,500 SwiftUI pages successfully
- Validated markdown quality and structure
- Refined scraping patterns and error handling

### Phase 2: Core Frameworks - COMPLETE
- Added UIKit, Foundation, Swift Standard Library
- Implemented cross-framework linking
- Optimized hash system with ETag support

### Phase 3: Full Coverage - COMPLETE
- Scraped all 373 frameworks systematically
- Implemented parallel scraping (10 concurrent connections)
- Deployed incremental update system with ETag optimization

### Phase 4: Meilisearch Migration - COMPLETE
- Migrated from ChromaDB to Meilisearch
- Achieved sub-500ms search times
- Implemented platform filtering

### Current Status: Production Deployed
- **Total documents**: 334,468 pages across 373 frameworks
- **Search**: Meilisearch for ultra-fast full-text search
- **MCP Server**: Deployed at http://192.168.2.5:8080/mcp/
- **Search performance**: <500ms with platform filtering
- **MCP Version**: 1.1.0 with wildcard search and stateful framework selection

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

## MCP Server Features (v1.1.0)

### Available Tools
| Tool | Description |
|------|-------------|
| `search_apple_docs` | Search documentation with wildcard support (`*`, `?`) |
| `expand_result` | Get full content for a symbol name or file path |
| `list_frameworks` | Browse frameworks with optional filtering |
| `choose_framework` | Set active framework to scope searches |
| `current_framework` | Show current framework selection |
| `get_version` | Get server version and status |

### Key Features
- Wildcard search: `*View`, `UI*`, `Button?`
- Stateful framework selection
- Platform filtering (ios, macos, tvos, watchos, visionos, all)
- Token budget management (1K-25K)
- Smart link transformation

## Success Metrics - ALL ACHIEVED
- All 373 frameworks indexed
- 334,468 pages with proper formatting
- Working cross-references between frameworks
- Efficient incremental updates via ETag optimization
- MCP server deployed and operational
- Meilisearch full-text search with <500ms response time
- Platform-aware filtering (iOS, macOS, tvOS, etc.)

## Current Status: COMPLETE & PUBLIC READY
- Scraping infrastructure complete
- All Apple documentation successfully indexed
- MCP server deployed with Docker
- Ready for public GitHub release
