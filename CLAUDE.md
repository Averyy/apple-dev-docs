# Claude Guidelines

## Project Overview

A comprehensive Python tool that scrapes Apple's entire developer documentation ecosystem, converts it into searchable vector embeddings, and provides an MCP (Model Context Protocol) server for AI-powered documentation search with platform-aware filtering.

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

### Scraping Best Practices

- Add delays between requests
- Use random User-Agent headers
- Log all scraping activities for debugging

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

### Key Technologies

- **Web Scraping**: httpx (async HTTP client) - that's it!
- **JSON Processing**: Built-in json module
- **Storage**: Local filesystem only (MVP)
- **Deployment**: Docker, with environment-based configuration

## Development Workflow

1. **Research Phase**
   - Analyze target website structure
   - Identify content patterns and selectors
   - Test scraping logic in Jupyter notebook first
   - Document legal structure of content

2. **Implementation**
   - Write scraper following base class pattern
   - Add proper error handling and logging
   - Test with small batches first
   - Validate legal context preservation

3. **Processing Setup**
   - Scrape documents and create simple chunks
   - Generate embeddings using Voyage-law-2
   - Build Chroma vector store
   - Contextual enrichment planned for future phase

3. **Testing**
   - Unit tests for parsers and extractors
   - Integration tests with real websites (sparingly)
   - Validate markdown output manually
   - Test SSE streaming with frontend
   - Verify source attributions are accurate

4. **Documentation**
   - Document CSS selectors and patterns for each source
   - Note any special handling required
   - Update source configuration
   - Track scraping patterns for reuse

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