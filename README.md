# 🍎 Apple Developer Documentation MCP Server

 An MCP (Model Context Protocol) server that gives Claude and other AI assistants access to Apple's complete developer documentation. Search across Apple's entire developer documentation - 370+ frameworks, 334,000+ pages, <500ms latency.

[![Frameworks](https://img.shields.io/badge/frameworks-370%2B-blue)](docs/MCP_COMPLETE_GUIDE.md)
[![Documents](https://img.shields.io/badge/documents-334K%2B-green)](docs/TECHNICAL_OPERATIONS_GUIDE.md)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

## 🤔 Why?

Apple's developer documentation website poses significant challenges for AI assistants and automated tools. The site uses aggressive lazy-loading techniques, rendering only visible content in the HTML source. This makes it nearly impossible for AI systems to effectively search or reference Apple's extensive documentation.

To bridge this gap and enhance the developer experience, this project provides a complete, searchable mirror of Apple's documentation in a clean, AI-friendly format. All content remains unchanged from the original source - we've simply made it accessible for modern AI-powered development workflows.

**Documentation last scraped:** December 21, 2025 (includes WWDC 2025 updates)

## ✨ Key Features

- 📚 **370+ Apple frameworks** - SwiftUI, UIKit, Metal, ARKit, Core ML, and more
- 🔍 **Smart semantic search** - Improved relevance scoring with framework awareness
- 🎯 **Platform & framework filtering** - iOS, macOS, tvOS, watchOS, visionOS + strict framework mode
- ⚡ **Fast responses** - Sub-500ms search powered by Meilisearch
- 📄 **Full documentation access** - Expand results to view complete content
- 🔗 **Smart link resolution** - Internal links converted to searchable queries
- 💡 **Token management** - Control response size (1K-25K tokens)
- 🤖 **MCP compatible** - Works with Claude Desktop, Claude Code, and other MCP clients
- 📍 **Stateful framework selection** - Set an active framework to scope all searches (v1.1.0)
- 🔤 **Wildcard search** - Use `*` and `?` patterns like `*View` or `UI*` (v1.1.0)

## 🔑 Environment Variables

### Required Variables
| Variable | Description | How to Generate |
|----------|-------------|-----------------|
| `MEILI_MASTER_KEY` | **REQUIRED** - Meilisearch authentication key | `openssl rand -hex 32` |

### Optional Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_API_KEY` | Authentication for remote HTTP access (recommended) | None |
| `ENABLE_HTTP_WRAPPER` | Enable HTTP endpoint for remote access | `true` (Docker) |
| `ENABLE_AUTO_RESCRAPE` | (Deprecated - Docker images include static documentation) | `false` |
| `HTTP_PORT` | Port for HTTP wrapper | `8080` |
| `MEILI_SEARCH_KEY` | Read-only search key (auto-generated from `MEILI_MASTER_KEY`) | None |
| `MEILI_ADMIN_KEY` | Admin operations key (auto-generated from `MEILI_MASTER_KEY`) | None |

## 🚀 Quick Start

### Option 1: Docker Deployment (All-in-One Container)

```bash
# 1. Clone the repository
git clone https://github.com/Averyy/apple-dev-docs.git
cd apple-dev-docs

# 2. Set up environment
cp .env.example .env

# 3. Edit .env and set REQUIRED variables:
MEILI_MASTER_KEY=your-generated-key-here  # Generate: openssl rand -hex 32

# 4. (Recommended) For secure remote access, also set:
MCP_API_KEY=your-generated-key-here       # Generate: openssl rand -hex 32

# 5. Build and run
cd mcp-server
docker-compose up -d --build

# Container automatically indexes on first run (~4 minutes)
# Check progress: docker logs -f apple-docs-mcp
# (All documentation is pre-included from December 21, 2025)

# ⚠️ INITIAL INDEXING: The first run will use significant CPU and memory
# for 5-10 minutes while indexing 334,000+ documents. This is normal!
# After indexing completes, resource usage drops to minimal levels.

# Server is now accessible at http://YOUR_SERVER_IP:8080/mcp
```

**Default Access:** The container enables HTTP access by default on port 8080. Set `MCP_API_KEY` for authentication.

**Data Persistence:** Docker uses named volumes (`meilisearch`, `logs`). Your search index persists across container restarts. Documentation is baked into the Docker image.

### Option 2: Local Development Setup

```bash
# 1. Clone and setup
git clone https://github.com/Averyy/apple-dev-docs.git
cd apple-dev-docs

# 2. Start Meilisearch
docker run -d -p 7700:7700 \
  -e MEILI_MASTER_KEY=$MEILI_MASTER_KEY \
  -v $(pwd)/meilisearch/data:/meili_data \
  getmeili/meilisearch:v1.9

# 3. Index documents (~4 minutes)
cd scripts && python3 index_to_meilisearch.py

# 4. Run MCP server
cd ../mcp-server && python3 apple_docs_stdio_mcp.py
```

## 📋 Configuration

### Claude Desktop/Code Configuration

**For local development:**
```json
{
  "mcpServers": {
    "apple-docs": {
      "command": "python3",
      "args": ["/path/to/apple-dev-docs/mcp-server/apple_docs_stdio_mcp.py"]
    }
  }
}
```

**For remote server (e.g., 192.168.2.5):**
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "stdio",
      "command": "python3",
      "args": [
        "/path/to/apple-dev-docs/apple_docs_remote_client.py",
        "--server-url",
        "http://192.168.2.5:8080/mcp",
        "--api-key",
        "your-mcp-api-key"
      ]
    }
  }
}
```

**Note:** 
- Claude Code only supports STDIO transport. The remote client script enables communication with remote HTTP servers while maintaining STDIO compatibility.
- For remote connections, the API key is passed as a command-line argument, not as an environment variable.
- The "type": "stdio" field is required for Claude Code compatibility.
- Initial connection to remote servers may take 10-30 seconds - this is normal.
- For Claude Code, add the configuration to your MCP settings (location varies by OS).

## 🔄 Manual Operations

### Updating Documentation

**⚠️ Note for Docker users:** The Docker image includes pre-scraped documentation from December 21, 2025. The scraping functionality is not available within the container to keep the image lightweight. To update documentation, you'll need to:

1. Run the scraper locally (see commands below)
2. Build a new Docker image with updated documentation
3. Deploy the new image

**For local development - Update all frameworks:**
```bash
python3 scrape.py --all --yes
```

**Update specific frameworks:**
```bash
python3 scrape.py --frameworks SwiftUI UIKit Foundation --yes
```

**Update with higher concurrency (default is 20):**
```bash
python3 scrape.py --all --yes --concurrent 30
```

**Update and automatically re-index Meilisearch:**
```bash
python3 scrape.py --all --yes --trigger-reindex
```

### Managing Orphaned Documentation

When Apple removes documentation pages, you can clean them up:

**Check and manually approve deletions (recommended):**
```bash
# After scraping completes, prompts once for all orphans
python3 scrape.py --all --yes --cleanup-orphans
```

**Auto-delete orphaned files (no prompts):**
```bash
python3 scrape.py --all --yes --cleanup-orphans --auto-cleanup
```

**Complete update with cleanup and re-indexing:**
```bash
python3 scrape.py --all --yes --cleanup-orphans --auto-cleanup --trigger-reindex
```

**Check orphans without scraping:**
```bash
python3 scripts/utilities/check_all_orphans.py
```

### Re-indexing to Meilisearch

After updating documentation, re-index to Meilisearch:

```bash
cd scripts && python3 index_to_meilisearch.py
```

**Note:** The Docker container handles indexing automatically on first run. Re-indexing is only needed after manual documentation updates.

## 🛠 Available Tools

### `search_apple_docs`
Search Apple's documentation with natural language queries.

**Parameters:**
- `query` - Your search query (required). Supports wildcards: `*` (any characters), `?` (single character)
- `framework` - Filter by framework (e.g., "SwiftUI", "UIKit"). If not specified, uses active framework if set.
- `strict_framework` - Only show results from specified framework (default: false, but true when using active framework)
- `platform` - Filter by platform: ios, macos, tvos, watchos, visionos, all (default: all)
- `limit` - Number of results (1-20, default: 10)
- `offset` - Pagination offset (default: 0)
- `token_budget` - Response size in tokens (1000-25000, default: 10000)
- `summary_mode` - Return condensed summaries (default: false)

**Example queries:**
- `"SwiftUI Button custom style"` - Smart relevance prioritizes core components
- `"async await URLSession"` - Finds modern async patterns
- `"*View"` - Wildcard search for all View types
- `"UI*Controller"` - Find UIKit controllers

### `expand_result`
Get the full content of a specific documentation file or symbol.

**Parameters:**
- `file_path` - Symbol name (e.g., "Button", "NavigationStack") or file path from search results. Uses active framework if set.
- `sections` - Optional: specific sections to extract

**Examples:**
- `expand_result { "file_path": "Button" }` - Look up Button symbol directly
- `expand_result { "file_path": "documentation/SwiftUI/View.md" }` - Full file path

### `list_frameworks`
Browse all 370+ available frameworks with document counts.

**Parameters:**
- `query` - Optional filter to search framework names (e.g., "UI", "Core", "Kit")

### `choose_framework`
Select a framework to scope all subsequent searches. Once set, searches default to this framework.

**Parameters:**
- `framework` - Framework name (e.g., "SwiftUI", "UIKit"). Use "clear" to remove selection.

**Examples:**
- `choose_framework { "framework": "SwiftUI" }` - Select SwiftUI
- `choose_framework { "framework": "clear" }` - Clear selection

### `current_framework`
Show the currently selected framework and available next steps.

### `get_version`
Get server version and status information including document counts.

## 📦 Requirements

- Python 3.11+ or Docker
- Meilisearch master key (for search engine)
- MCP API key (for remote deployments only, not required for local)
- 1.5GB RAM (4GB+ recommended during initial indexing)
- 1GB disk space
- CPU: High usage during indexing (5-10 min), minimal afterwards

## 🔧 Advanced Configuration

### Remote Client Configuration

The remote client script enables Claude Code (STDIO-only) to connect to remote HTTP servers:

```bash
# Test remote connection manually
python3 apple_docs_remote_client.py --server-url http://192.168.2.5:8080/mcp --api-key your-key --test
```

### Unraid Installation

For Unraid users:
1. Add template repository: `https://github.com/Averyy/apple-dev-docs/tree/main/unraid`
2. Install "apple-docs-mcp" from Community Applications
3. Configure with required environment variables
4. Add the container paths for persistent data

## 🤝 Contributing

Contributions welcome! Please check the docs folder for technical details.

## 📄 License

**Code**: MIT License  
**Documentation Content**: © Apple Inc. - For development use only