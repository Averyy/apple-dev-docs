# Private Memory - Backend Development Agent

## Apple Documentation Scraper Project - COMPLETED ✅

### Project Stats (Current as of December 2025)
- **Scale**: 373 frameworks, 334,468 documents
- **Search Engine**: Meilisearch for ultra-fast full-text search
- **Cost**: ~$5.00 USD initial embedding generation (legacy, no longer needed with Meilisearch)
- **Deployment**: Production at 192.168.2.5 (Docker)
- **Performance**: <500ms search with platform filtering

### Technical Implementation
- **Scraping**: Uses Apple's JSON API (not HTML)
- **Search**: Meilisearch for ultra-fast full-text search (migrated from ChromaDB)
- **MCP Server**: STDIO-based with optional HTTP wrapper for remote access
- **Transport**: STDIO for Claude Code, HTTP wrapper for remote access

### Completed Milestones
1. ✅ Built JSON-based scraper (no Puppeteer needed)
2. ✅ Scraped all 373 frameworks successfully (includes WWDC 2025)
3. ✅ Implemented SHA-256 hash deduplication
4. ✅ Created production MCP server
5. ✅ Deployed with Docker
6. ✅ Migrated from ChromaDB to Meilisearch

### MCP Server Features (v1.1.0)
- Stateful framework selection (`choose_framework`, `current_framework`)
- Wildcard search support (`*View`, `UI*`, `Button?`)
- `get_version` tool for status information
- Enhanced `expand_result` to accept symbol names
- Platform filtering (ios, macos, tvos, watchos, visionos, all)

### Key URLs
- Main docs: https://developer.apple.com/documentation
- GitHub repo: https://github.com/Averyy/apple-dev-docs
- Production server: http://192.168.2.5:8080/mcp/
