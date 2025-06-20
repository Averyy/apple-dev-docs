# Claude Guidelines

## Deployment Testing Instructions

**CRITICAL: How to test the deployed MCP server at 192.168.2.5**

The deployed server requires specific parameters and flow:

1. **Protocol Version**: Must use `"2024-11-05"` not `"1.0.0"`
2. **Session Management**: Server returns session ID in `mcp-session-id` header after initialize
3. **SSE Responses**: All responses are Server-Sent Events format: `data: {json}`
4. **Link Transformation**: Only visible with `include_full_content: True` parameter
5. **Required Headers**: 
   - `Authorization: Bearer $MCP_API_KEY`
   - `Accept: application/json, text/event-stream`
   - `MCP-Session-Id: {session_id}` (after initialize)

Correct test sequence:
```bash
# Test the deployed server
cd mcp-server && python3 tests/test_deployed_server.py
```

Common mistakes to avoid:
- Using wrong protocol version
- Not including session ID in subsequent requests
- Forgetting `include_full_content: True` when testing link transformation
- Not parsing SSE responses correctly

## Project Overview

A comprehensive Python tool that scrapes Apple's entire developer documentation ecosystem, converts it into searchable vector embeddings, and provides an MCP (Model Context Protocol) server for AI-powered documentation search with platform-aware filtering.

**Main Problem**: Mirror Apple's complete developer documentation for offline semantic search via MCP server integration.

## Critical Rules - DO NOT VIOLATE

- **NEVER create mock data or simplified components** unless explicitly told to do so
- **NEVER replace existing complex components with simplified versions** - always fix the actual problem
- **ALWAYS work with the existing codebase** - do not create new simplified alternatives
- **ALWAYS find and fix the root cause** of issues instead of creating workarounds
- When debugging issues, focus on fixing the existing implementation, not replacing it
- When something doesn't work, debug and fix it - don't start over with a simple version
- If anything is unclear or you're not sure - ask
- **NEVER** impersonate people and team members, do the role you are assigned and don't reply as if you're someone else
- When fixing bugs or implementing changes, UPDATE THE EXISTING FILES, don't create new files unless absolutely necessary.
- Don't update THIS file with project status, this is only for the rules you must follow
- Always look up documentation (either via context7 mcp or web search) when unsure
- One time use files for debugging should be put in a temp folder or labelled temp_ so we know later that they are safe to delete
- **ALWAYS use relative paths in scripts** - never use absolute paths, use proper relative path resolution
- MCP server setup should **always** follow the latest spec from https://modelcontextprotocol.io/specification/
- **NEVER SUGGEST SPECIAL HANDLING FOR SPECIFIC PATTERNS** - The codebase has 360+ frameworks. Do not suggest adding special cases for individual APIs, common patterns, or specific query types. This approach does not scale.

### Python Development Standards

- Use Python 3.11+ with type hints for all functions
- Follow PEP 8 style guidelines
- Use `asyncio` for concurrent operations
- Always validate scraped data before processing
- Use proper logging (not print statements)
- Run `mypy` for type checking before considering code complete
- Optimize for performance
- Design for memory efficiency with URL cache cleanup
- Design for multiple concurrent users from day one

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

## Project Architecture

### Core Components

1. **Generic JSON Scraper**: Single scraper that works for ALL Apple frameworks
2. **URL Discovery**: Traverse JSON references to find all documentation pages
3. **JSON to Markdown Converter**: Transform structured JSON to clean markdown
4. **Hash Manager**: Track changes and avoid duplicate scraping
5. **Progress Tracker**: Monitor completion across all frameworks

### Core Technologies

- **Apple JSON API**: Direct access to structured documentation data
- **Embeddings**: OpenAI text-embedding-3-small (1536 dimensions)
- **Vector Database**: ChromaDB (local storage)
- **MCP Server**: FastAPI with Bearer token authentication
- **Processing**: httpx async client, built-in JSON processing

## MCP Server Features

- **Platform Filtering**: Required parameter (ios, macos, tvos, watchos, visionos, catalyst, all)
- **Framework Discovery**: `list_frameworks` tool with summaries and availability
- **Sub-500ms Search**: Optimized ChromaDB queries with metadata filtering
- **Bearer Authentication**: API key required for all endpoints

## Core Commands

```bash
# Environment setup
cp .env.example .env  # Edit to add API keys

# Run scraper
python scrape.py --all --yes

# Rebuild vectorstore with metadata
cd mcp-server && python scripts/build_index.py --force

# Run MCP server  
cd mcp-server && make server

# Health check
cd mcp-server && python tests/test_mcp_server.py
```

## Project Structure

```
apple-developer-docs/
├── .env                           # Environment variables (API keys)
├── scrape.py                      # Main documentation scraper
├── documentation/                 # Scraped markdown files
├── vectorstore/                   # ChromaDB storage (main)
├── tests/                         # Top-level test suite
├── scripts/                       # Utility scripts
└── mcp-server/                    # MCP server implementation
    ├── scripts/build_index.py     # Embedding generation with metadata
    ├── server/mcp_server.py       # FastAPI MCP server
    ├── server/rag.py              # Search engine with platform filtering
    ├── vectorstore/               # ChromaDB storage (MCP server)
    └── tests/                     # MCP server tests
```