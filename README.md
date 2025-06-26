# 🍎 Apple Developer Documentation MCP Server

 An MCP (Model Context Protocol) server that gives Claude and other AI assistants access to Apple's complete developer documentation. Search across Apple's entire developer documentation - 360 frameworks, 340,000+ pages, <500ms latency.

[![Frameworks](https://img.shields.io/badge/frameworks-360-blue)](docs/MCP_COMPLETE_GUIDE.md)
[![Documents](https://img.shields.io/badge/documents-340K%2B-green)](docs/TECHNICAL_OPERATIONS_GUIDE.md)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

## 🤔 Why?

Apple's developer documentation website poses significant challenges for AI assistants and automated tools. The site uses aggressive lazy-loading techniques, rendering only visible content in the HTML source. This makes it nearly impossible for AI systems to effectively search or reference Apple's extensive documentation.

To bridge this gap and enhance the developer experience, this project provides a complete, searchable mirror of Apple's documentation in a clean, AI-friendly format. All content remains unchanged from the original source - we've simply made it accessible for modern AI-powered development workflows.

**Documentation last scraped:** Thursday, June 26, 2025 (after the WWDC updates)

## ✨ Key Features

- 📚 **360+ Apple frameworks** - SwiftUI, UIKit, Metal, ARKit, Core ML, and more
- 🔍 **Smart semantic search** - Improved relevance scoring with framework awareness
- 🎯 **Platform & framework filtering** - iOS, macOS, tvOS, watchOS, visionOS + strict framework mode
- ⚡ **Fast responses** - Sub-500ms search powered by Meilisearch
- 📄 **Full documentation access** - Expand results to view complete content
- 🔗 **Smart link resolution** - Internal links converted to searchable queries
- 💡 **Token management** - Control response size (1K-25K tokens)
- 🤖 **MCP compatible** - Works with Claude Desktop, Claude Code, and other MCP clients

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
| `ENABLE_AUTO_RESCRAPE` | Enable weekly documentation updates | `false` |
| `KEEP_MARKDOWN_FILES` | Keep source markdown files (uses 2GB extra) | `false` |
| `HTTP_PORT` | Port for HTTP wrapper | `8080` |
| `MEILI_SEARCH_KEY` | Read-only search key (auto-generated from `MEILI_MASTER_KEY`) | None |
| `MEILI_ADMIN_KEY` | Admin operations key (auto-generated from `MEILI_MASTER_KEY`) | None |

## 🚀 Quick Start

### Option 1: Docker Deployment (All-in-One Container)

```bash
# 1. Clone the repository
git clone https://github.com/averyy/apple-developer-docs.git
cd apple-developer-docs

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
# (All documentation is already included and up to date)

# Server is now accessible at http://YOUR_SERVER_IP:8080/mcp
```

**Default Access:** The container enables HTTP access by default on port 8080. Set `MCP_API_KEY` for authentication.

**Data Persistence:** Docker uses named volumes (`meilisearch`, `documentation`, `hashes`, `logs`). Your data persists across container restarts.

### Option 2: Local Development Setup

```bash
# 1. Clone and setup
git clone https://github.com/averyy/apple-developer-docs.git
cd apple-developer-docs

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
      "args": ["/path/to/apple-developer-docs/mcp-server/apple_docs_stdio_mcp.py"]
    }
  }
}
```

**For remote server (e.g., 192.168.2.5):**
```json
{
  "mcpServers": {
    "apple-docs": {
      "command": "python3",
      "args": [
        "/path/to/apple-developer-docs/mcp-server/apple_docs_stdio_http_bridge.py",
        "--server-url", "http://192.168.2.5:8080/mcp"
      ],
      "env": {
        "MCP_API_KEY": "your-mcp-api-key"
      }
    }
  }
}
```

**Note:** 
- Claude Code only supports STDIO transport. The bridge script enables communication with remote HTTP servers while maintaining STDIO compatibility.
- MCP_API_KEY is ONLY required for remote deployments. Local STDIO mode does not require it.
- For Claude Code add to `../mcp_servers.json`:

## 🛠 Available Tools

### `search_apple_docs`
Search Apple's documentation with natural language queries.

**Parameters:**
- `query` - Your search query (required)
- `framework` - Filter by framework (e.g., "SwiftUI", "UIKit")
- `strict_framework` - Only show results from specified framework (default: false)
- `platform` - Filter by platform: ios, macos, tvos, watchos, visionos, all (default: all)
- `limit` - Number of results (1-20, default: 10)
- `offset` - Pagination offset (default: 0)
- `token_budget` - Response size in tokens (1000-25000, default: 10000)
- `summary_mode` - Return condensed summaries (default: false)

**Example queries:**
- "SwiftUI Button custom style" - Smart relevance prioritizes core components
- "async await URLSession" - Finds modern async patterns
- "MapKit annotations" - Returns results with internal links as search hints

### `expand_result`
Get the full content of a specific documentation file.

**Parameters:**
- `file_path` - Path from search results (supports both absolute and relative paths)
- `sections` - Optional: specific sections to extract

### `list_frameworks`
Browse all 360 available frameworks with document counts.

## 📦 Requirements

- Python 3.11+ or Docker
- Meilisearch master key (for search engine)
- MCP API key (for remote deployments only, not required for local)
- 1.5GB RAM
- 1GB disk space

## 🔧 Advanced Configuration

### STDIO-to-HTTP Bridge

The bridge script enables Claude Code (STDIO-only) to connect to remote HTTP servers:

```bash
# Test bridge manually
cd mcp-server
python3 apple_docs_stdio_http_bridge.py --server-url http://192.168.2.5:8080/mcp --api-key your-key --debug
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