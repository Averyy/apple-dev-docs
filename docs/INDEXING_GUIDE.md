# Vector Index Building Guide

This guide explains how to build and maintain the vector index for Apple Developer Documentation.

## Prerequisites

1. **Environment Setup**: Complete Task 01 (environment setup)
2. **Documentation Files**: Ensure the scraper has completed downloading documentation
3. **Voyage AI API Key**: Get from https://www.voyageai.com/ and add to `.env`
4. **Virtual Environment**: Always activate the venv before running commands

## Quick Start

```bash
# Navigate to mcp-server directory
cd mcp-server

# Activate virtual environment
source venv/bin/activate

# Run initial indexing
make index

# Monitor progress in another terminal
make monitor
```

## Full Indexing Process

### Step 1: Validate Documentation

Before indexing, ensure documentation is properly downloaded:

```bash
make validate
```

Expected output:
- ~341 frameworks
- ~278,778 markdown files
- Total size: ~1.17GB

### Step 2: Start Indexing

For initial indexing:
```bash
make index
```

For force rebuild (clears existing index):
```bash
make index-force
```

### Step 3: Monitor Progress

In a separate terminal:
```bash
make monitor
```

This shows:
- Documents indexed
- Processing speed (expect ~32 docs/sec)
- Memory usage (should stay under 200MB)
- ETA for completion

### Step 4: Verify Index

After completion:
```bash
make index-verify
```

## Incremental Updates

The indexer automatically detects changes:
- New files are added
- Modified files are re-indexed
- Deleted files are removed from index

Just run `make index` to update.

## Performance Expectations

Using Voyage-3-lite API:
- **Speed**: ~30-40 documents/second
- **Total time**: 2-3 hours for 278K documents
- **Memory usage**: ~100-200MB
- **Vectorstore size**: ~0.6GB (512 dimensions)
- **API cost**: ~$0.83 for full indexing

## Troubleshooting

### NumPy Compatibility Error
If you see `np.float_` errors, ensure you're using the virtual environment:
```bash
source venv/bin/activate
```

### Slow Indexing
- Check your internet connection (API calls to Voyage)
- Ensure no rate limit errors in logs
- Monitor with `make monitor` to track progress

### Recovery from Interruption
The indexer automatically recovers from interruptions:
1. Just run `make index` again
2. It will resume from where it left off
3. Use `make test-recovery` to test this functionality

### Memory Issues
If memory usage is high:
1. The batch size is already optimized (100 files)
2. Check for other memory-intensive processes
3. Consider closing other applications

## Testing

Before running full indexing:
```bash
# Test with sample documents
make test-index

# Test recovery mechanism
make test-recovery
```

## File Structure

After indexing, the vectorstore contains:
```
vectorstore/
├── chroma.sqlite3         # ChromaDB database
├── file_hashes.json       # Tracks file changes
├── indexing_metrics.json  # Performance metrics
└── indexing_summary.json  # Final summary
```

## Cost Analysis

Using Voyage-3-lite API:
- **Embedding cost**: ~$0.83 (one-time)
- **Time cost**: 2-3 hours
- **Storage**: ~0.6GB for vectors
- **Dimensions**: 512 (optimized for speed)

Alternatives:
- BGE-M3 via TEI: $0 but requires GPU server
- OpenAI ada-002: ~$5.86 (7x more expensive)

## Maintenance

### Regular Updates
Run weekly or after major documentation updates:
```bash
make index  # Only processes changes
```

### Full Rebuild
Only needed if index corruption suspected:
```bash
make clean
make index-force
```

### Backup
Backup the vectorstore directory regularly:
```bash
tar -czf vectorstore_backup_$(date +%Y%m%d).tar.gz vectorstore/
```

## Integration with Task 03

Once indexing is complete, the RAG engine (Task 03) can:
- Query the ChromaDB collection
- Use Voyage AI for query embeddings
- Return relevant documentation chunks

The index is optimized for:
- One embedding per documentation file
- Fast similarity search (512 dimensions)
- Framework-based filtering
- Metadata-rich results
- 32K context window support