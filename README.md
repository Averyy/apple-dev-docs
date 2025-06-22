# Apple Developer Documentation MCP Server

> 🍎 **AI-powered search across Apple's entire developer documentation** - 341 frameworks, 340,000+ pages, <500ms search

[![Frameworks](https://img.shields.io/badge/frameworks-341-blue)](docs/MCP_COMPLETE_GUIDE.md)
[![Documents](https://img.shields.io/badge/documents-340K%2B-green)](docs/TECHNICAL_OPERATIONS_GUIDE.md)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

## 🚀 What is this?

An MCP (Model Context Protocol) server that gives Claude and other AI assistants access to Apple's complete developer documentation. Ask questions in natural language and get instant, accurate answers from official Apple docs.

### Example

```
You: How do I create a SwiftUI button with a gradient background?
Claude: Let me search the Apple documentation for SwiftUI Button styling...

[Returns official Apple documentation with code examples, modifiers, and platform availability]
```

## ✨ Key Features

- 📚 **341 Apple frameworks** - SwiftUI, UIKit, Metal, ARKit, Core ML, and more
- 🔍 **Semantic search** - Understands natural language queries
- 🎯 **Platform filtering** - iOS, macOS, tvOS, watchOS, visionOS, Catalyst
- ⚡ **Fast responses** - Sub-500ms search with vector embeddings
- 🔄 **Auto-updates** - Weekly synchronization with Apple's latest docs
- 🤖 **MCP compatible** - Works with Claude Desktop, Claude Code, and other MCP clients

## 🚀 Quick Start

### Option 1: Connect to My Server (Easiest)

```bash
# Download the client
curl -O https://raw.githubusercontent.com/averyy/apple-developer-docs/main/apple_docs_remote_client.py

# Add to Claude (see Configuration section below)
```

### Option 2: Run Your Own Server

```bash
# Quick Docker deployment
git clone https://github.com/averyy/apple-developer-docs.git
cd apple-developer-docs
cp .env.example .env
# Add your OPENAI_API_KEY to .env
cd mcp-server/deploy && ./quick-start.sh
```

## 📋 Configuration

### Claude Desktop
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "stdio",
      "command": "python3",
      "args": ["/path/to/apple_docs_remote_client.py"]
    }
  }
}
```

### Claude Code  
Add to `.claude/mcp_servers.json`:
```json
{
  "apple-docs": {
    "type": "stdio",
    "command": "python3",
    "args": ["/path/to/apple_docs_remote_client.py"]
  }
}
```

## 🛠 Available Tools

### `search_apple_docs`
Search Apple's documentation with natural language queries.

**Example queries:**
- "Button in SwiftUI" - Framework-specific search
- "async await" - Cross-framework concept search
- "navigationBarTitle NavigationView" - Multi-term for precise results

### `list_frameworks`
Browse all 341 available frameworks by platform.

## 📦 Requirements

- Python 3.11+
- OpenAI API key (for embeddings only - ~$5 one-time cost)
- 2GB RAM for vector index
- 2GB disk space

## 📚 Documentation

- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md) - Docker setup and deployment
- [Technical Guide](docs/TECHNICAL_OPERATIONS_GUIDE.md) - Architecture and operations
- [MCP Guide](docs/MCP_COMPLETE_GUIDE.md) - API reference and usage
- [Security Guide](docs/SECURITY_GUIDE.md) - Best practices

## 🤝 Contributing

Contributions welcome! Please check the docs folder for technical details.

## 📄 License

**Code**: MIT License  
**Documentation Content**: © Apple Inc. - For development use only

---

<p align="center">Made with ❤️ for the Apple developer community</p>