# xdocs - Apple Developer Documentation MCP Server

> **Note:** This is an independent project not affiliated with, endorsed by, or sponsored by Apple Inc. Documentation content is © Apple Inc. and provided for development use only.

An MCP server that gives Claude and other AI assistants instant access to Apple's complete developer documentation. 370+ frameworks, 334K+ documents, sub-3ms search.

[![Frameworks](https://img.shields.io/badge/frameworks-370%2B-blue)](https://xdocs.dev)
[![Documents](https://img.shields.io/badge/documents-334K%2B-green)](https://xdocs.dev)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

## Quick Start

### Claude Code

```bash
claude mcp add --transport http apple-docs https://xdocs.dev/mcp
```

### Claude Desktop

1. Open Claude Desktop
2. Go to **Settings → Connectors**
3. Click **"Add custom connector"**
4. Name: `apple-docs`
5. URL: `https://xdocs.dev/mcp`
6. Click **Add**

### Cursor

Add to Cursor Settings → MCP:
```json
{
  "apple-docs": {
    "url": "https://xdocs.dev/mcp"
  }
}
```

### VSCode

Create `.vscode/mcp.json`:
```json
{
  "servers": {
    "apple-docs": {
      "type": "http",
      "url": "https://xdocs.dev/mcp"
    }
  }
}
```

### Other MCP Clients

For stdio-only clients, use `mcp-remote` as a bridge:
```json
{
  "mcpServers": {
    "apple-docs": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://xdocs.dev/mcp"]
    }
  }
}
```

## Why?

Apple's developer documentation website uses aggressive lazy-loading, rendering only visible content in the HTML source. This makes it nearly impossible for AI systems to effectively search or reference Apple's documentation.

This project provides a complete, searchable mirror of Apple's documentation in a clean, AI-friendly format. All content is unchanged from the original source - we've simply made it accessible.

**Last updated:** December 2025 (includes WWDC 2025)

## Features

- **370+ frameworks** - SwiftUI, UIKit, Metal, ARKit, Core ML, and more
- **Sub-3ms search** - Powered by Meilisearch
- **Platform filtering** - iOS, macOS, tvOS, watchOS, visionOS
- **Wildcard search** - `*View`, `UI*Controller`, `Button?`
- **Token management** - 1K-25K token budgets
- **Native HTTP** - Streamable HTTP transport (no wrappers needed)

## Available Tools

### `search_apple_docs`
Search documentation with natural language queries.

```
query: "SwiftUI Button custom style"
framework: "SwiftUI" (optional)
platform: "ios" (optional)
limit: 10 (1-20)
```

### `expand_result`
Get full documentation for a symbol.

```
file_path: "Button" or "documentation/SwiftUI/View.md"
```

### `list_frameworks`
Browse all 370+ frameworks with document counts.

```
query: "UI" (optional filter)
```

### `choose_framework`
Set active framework for subsequent searches.

```
framework: "SwiftUI" or "clear"
```

## Self-Hosting

### Docker (Recommended)

```bash
# Clone
git clone https://github.com/Averyy/apple-dev-docs.git
cd apple-dev-docs

# Configure
cp .env.example .env
# Edit .env: set MEILI_MASTER_KEY (run: openssl rand -hex 32)

# Run
cd mcp-server
docker-compose up -d

# Server available at http://localhost:8000/mcp
# First run indexes ~334K docs (~4 minutes)
```

### Local Development

```bash
# Install dependencies
pip install -r mcp-server/requirements.txt

# Start Meilisearch
docker run -d -p 7700:7700 \
  -e MEILI_MASTER_KEY=$(openssl rand -hex 32) \
  -v $(pwd)/meilisearch:/meili_data \
  getmeili/meilisearch:v1.9

# Index documents (~4 minutes)
cd scripts && python3 index_to_meilisearch.py

# Run server
cd ../mcp-server && python3 apple_docs_mcp.py
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MEILI_MASTER_KEY` | Yes | Meilisearch auth key (`openssl rand -hex 32`) |
| `MCP_API_KEY` | No | API key for rate limit bypass |
| `HTTP_PORT` | No | Server port (default: 8000) |

## Updating Documentation

```bash
# Scrape all frameworks
python3 scrape.py --all --yes

# Re-index to Meilisearch
cd scripts && python3 index_to_meilisearch.py
```

## Requirements

- Python 3.11+ or Docker
- 1.5GB RAM (4GB+ recommended for indexing)
- 1GB disk space

## License

**Code**: MIT License
**Documentation Content**: © Apple Inc. - For development use only

## Links

- **Website**: [xdocs.dev](https://xdocs.dev)
- **GitHub**: [github.com/Averyy/apple-dev-docs](https://github.com/Averyy/apple-dev-docs)
- **Contact**: info@xdocs.dev
