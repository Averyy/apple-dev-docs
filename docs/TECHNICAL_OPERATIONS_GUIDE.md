# Technical & Operations Guide

## 🏗️ System Architecture

### Core Components

1. **Scraping System** - Complete (341,207 files scraped)
   - Uses Apple's JSON API endpoints
   - ETag-based change detection
   - SHA-256 content hashing
   
2. **Embedding System** - Production Ready
   - OpenAI text-embedding-3-small (1536 dimensions)
   - ChromaDB vector storage (1.9GB)
   - 323,118 embeddings generated
   - Incremental processing with checkpointing
   
3. **Document Processing**
   - Automatic splitting for files >30KB
   - Preserves context with title inclusion
   - Chunk metadata tracking
   - ~18,500 large files split into chunks

4. **RAG Engine** - Complete
   - Located at `mcp-server/server/rag.py`
   - Sub-500ms search performance
   - Framework filtering support
   - Query expansion capabilities
   - Multi-search with deduplication

5. **MCP Server** - Deployed
   - Production endpoint: 192.168.2.5
   - FastAPI with Bearer token authentication
   - Docker containerized deployment
   - Unraid compatible

## ⚠️ CRITICAL: ChromaDB Configuration

### Always Use OpenAI Embeddings

**IMPORTANT**: Always use OpenAI embeddings (text-embedding-3-small, 1536 dimensions) for consistency:

```python
from chromadb.utils import embedding_functions

# ALWAYS use this configuration:
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv('OPENAI_API_KEY'),
    model_name='text-embedding-3-small',
    dimensions=1536
)

# When creating collections:
collection = client.create_collection(
    name='apple_docs_{framework}',
    embedding_function=embedding_function
)

# When getting collections (must specify same function):
collection = client.get_collection(
    name='apple_docs_{framework}',
    embedding_function=embedding_function
)
```

**Why this is critical:**
- ChromaDB's default creates 384-dimension vectors
- OpenAI creates 1536-dimension vectors
- Mixing causes: `Collection expecting embedding with dimension of 1536, got 384`
- Once created with one function, cannot query with another

## 🚀 Production Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY="sk-..."
MCP_API_KEY="your-bearer-token"  # For MCP server authentication

# Optional (with defaults)
MAX_EMBEDDING_COST="10.00"      # Hard cost limit
MAX_FILES_TO_EMBED="300000"      # File limit
MAX_FILE_SIZE_MB="10"            # Individual file size
MAX_TOKENS_PER_DOC="8000"        # Before splitting
OPENAI_RPM="3000"                # Rate limit
EMBEDDING_BATCH_SIZE="100"       # Batch size

# Scraper Configuration (optional)
MAX_CONCURRENT_REQUESTS="5"      # Concurrent HTTP requests (default: 5)
RATE_LIMIT_DELAY="0.2"          # Delay between requests in seconds (default: 0.2)
```

### Rate Limiting
- Default: 3000 requests/minute
- Automatic backoff on 429 errors
- Configurable delays between requests

### Error Recovery
1. **Network errors**: Exponential backoff with retry
2. **API errors**: Checkpoint and resume
3. **File errors**: Skip and log, continue processing
4. **Cost overrun**: Immediate abort with checkpoint

## 📄 Document Splitting Strategy

### Implementation
```python
def split_by_headers(content: str, max_tokens: int = 7000) -> List[str]:
    """Split large markdown documents by ## headers"""
    # Check if splitting needed
    if len(content) > 30000:  # ~7.5k tokens
        chunks = split_by_headers(content, max_tokens=7000)
        # Each chunk gets its own embedding with metadata
```

### Key Points
- **Source files are NEVER modified** - splitting only during embedding
- **Threshold**: Files >30KB (approximately 7,500 tokens)
- **Method**: Split by `## ` headers while preserving title
- **Impact**: ~18,500 files split into chunks
- **Benefits**: 
  - Optimized storage (1.9GB vs potential 17GB+)
  - Better search relevance
  - Focused context for LLMs

### Chunk Metadata Structure
```python
{
    "framework": "HomeKit",
    "api_name": "mtrattributeidtype",
    "file_path": "documentation/HomeKit/mtrattributeidtype.md",
    "file_size": 461235,
    "chunk_index": 0,
    "total_chunks": 3,
    "chunk_hash": "abc123..."
}
```

## 🔧 ChromaDB Best Practices

### 1. Collection Name Requirements
- Must be 3-63 characters long
- Start/end with alphanumeric characters
- Only alphanumeric, underscores, or hyphens
- Pattern: `apple_docs_{framework}`

### 2. Document ID Format
```python
# Standard document
"{filename}_{path_hash}_{content_hash}"

# Chunked document
"{filename}_{path_hash}_{content_hash}_part{index}"
```

### 3. Metadata Constraints
- Keys must be strings
- Values: strings, integers, floats, or booleans
- No nested objects or arrays
- Reserved keys: `id`, `embedding`, `document`

### 4. Batch Processing
- Maximum batch size: 41,666 documents
- Recommended: 100-1000 per batch
- Cost calculation per batch for safety

## 🔄 Incremental Update System

### Change Detection Flow
1. **Check ETag** (HTTP header from Apple)
2. **Compare content hash** if ETag unavailable
3. **Process only changed files**
4. **Update hash registry**

### Hash Storage Structure
```
.hashes/
├── {framework}_hashes.json  # Per-framework hashes
├── embedding_hashes.json    # Processed file tracking
└── embedding_checkpoint.json # Resume capability
```

### Deletion Handling
```python
# Pattern matching for chunks
base_pattern = f"{file.stem}_{path_hash}_"
old_ids = [id for id in existing_ids 
          if id.startswith(base_pattern) and id not in new_ids]
```

## 🗑️ Orphan Detection and Cleanup

### Automatic Cleanup
The scraper now automatically detects and removes orphaned documentation files when Apple removes pages:

1. **During Scraping**: Each file's location is tracked in the hash file
2. **After Completion**: Compares file timestamps with scrape start time
3. **Cleanup**: Deletes files that weren't updated (meaning they no longer exist on Apple's site)
4. **Empty Directories**: Automatically removed

### Manual Orphan Check
```bash
# Check all frameworks for orphans (dry run)
python3 scripts/check_orphans.py

# Check specific framework
python3 scripts/check_orphans.py --framework SwiftUI

# Actually delete orphaned files
python3 scripts/check_orphans.py --clean

# Show summary only
python3 scripts/check_orphans.py --summary

# Consider files orphaned if not updated in X days
python3 scripts/check_orphans.py --days 30
```

## 🔍 RAG Engine Details

### SimpleRAG Class (`mcp-server/server/rag.py`)
```python
class SimpleRAG:
    # Initialization
    - ChromaDB client with persistent storage
    - OpenAI client for query embeddings
    - Collection: "apple_docs" with 323,118 documents
    
    # Core Methods
    - search(): Main search with framework filtering
    - get_api_doc(): Direct API documentation lookup
    - multi_search(): Combined search with deduplication
    - expand_query(): Simple keyword expansion
    - format_for_mcp(): Claude-optimized formatting
```

### Search Performance
- **Average query time**: ~350ms
- **Vector similarity**: Cosine distance
- **Result limit**: 1-20 configurable
- **Deduplication**: Based on file_path

### Query Enhancement
Simple keyword expansion without LLM:
- "swiftui" → "SwiftUI View"
- "async" → "async await Task concurrency"
- "list" → "List ForEach ScrollView"

## 🏥 Health Monitoring System

### Daily Health Check
```bash
# Full system health check
python3 scripts/vectorstore_health_check.py --collection all

# Check specific framework
python3 scripts/vectorstore_health_check.py --collection apple_docs_SwiftUI

# Generate health report
python3 scripts/vectorstore_health_check.py --output health_report.json
```

### Health Check Components

1. **Orphaned Embeddings Detection**
   - Finds embeddings without corresponding source files
   - Automatic cleanup with `--fix` flag

2. **Missing Embeddings Detection**
   - Identifies documents not yet embedded
   - Reports coverage percentage

3. **Content Synchronization**
   - Verifies embedded content matches source
   - Detects corrupted embeddings

4. **Embedding Integrity**
   - Validates vector dimensions (1536)
   - Checks for null or invalid embeddings

5. **Metadata Completeness**
   - Ensures all required fields present
   - Validates metadata format

### Health Status Indicators
- ✅ **PASS**: No issues found
- ⚠️ **INFO**: Informational, no action needed  
- ❌ **FAIL**: Issues requiring attention

## 💾 Backup and Recovery

### Automated Backup System
```bash
# Create backup with verification
python3 scripts/backup_vectorstore.py --create

# Restore from backup
python3 scripts/backup_vectorstore.py --restore backup_20240610_120000.tar.gz

# Verify backup integrity
python3 scripts/backup_vectorstore.py --verify backup_20240610_120000.tar.gz
```

### Backup Features
- **Compression**: ~70% size reduction
- **Integrity Check**: MD5 verification
- **Metadata Preservation**: Timestamps and permissions
- **Safe Restore**: Backs up current state before restoring

### Backup Schedule (Recommended)
```bash
# Add to crontab
0 2 * * * cd /path/to/project && python3 scripts/backup_vectorstore.py --create
```

## 🔄 Daily Operations

### Daily Update Process
```bash
# Run incremental update (safe, only processes changes)
python3 scripts/build_index_incremental.py --force

# Update specific framework
python3 scripts/build_index_incremental.py --framework SwiftUI --force
```

### Monitoring Update Progress
- Real-time progress bar
- Cost tracking display
- File processing count
- Checkpoint status updates

### Update Automation
```bash
# Cron job for daily updates at 3 AM
0 3 * * * cd /path/to/project && python3 scripts/build_index_incremental.py --force >> logs/daily_update.log 2>&1
```

## 📊 Production Monitoring

### Real-Time Monitoring
```bash
# Monitor system health via health check
python3 scripts/vectorstore_health_check.py

# Generate detailed health report
python3 scripts/vectorstore_health_check.py --output health_report.json
```

### Key Metrics to Monitor
1. **Embedding Rate**: Files processed per minute
2. **Error Rate**: Failed embeddings percentage
3. **Storage Usage**: Vectorstore size growth
4. **API Usage**: OpenAI API calls and costs
5. **Memory Usage**: System resource consumption

### Alert Thresholds
- Error rate > 1%: Investigate issues
- Storage > 2GB: Consider cleanup
- Cost > $5/day: Review update frequency
- Memory > 80%: Scale resources

## 🚨 Emergency Procedures

### 1. Embedding Process Hangs
```bash
# 1. Check checkpoint status
cat .hashes/embedding_checkpoint.json

# 2. Kill process (safe - will resume from checkpoint)
pkill -f build_index_incremental.py

# 3. Resume from checkpoint
python3 scripts/build_index_incremental.py
```

### 2. Corrupted Vector Store
```bash
# 1. Stop all processes
pkill -f build_index

# 2. Restore from latest backup
python3 scripts/backup_vectorstore.py --restore latest

# 3. Run health check
python3 scripts/vectorstore_health_check.py --fix
```

### 3. Cost Overrun
```bash
# 1. Set lower cost limit
export MAX_EMBEDDING_COST="1.00"

# 2. Process in smaller batches
python3 scripts/build_index_incremental.py --framework SmallFramework

# 3. Monitor costs closely
# Check .hashes/embedding_checkpoint.json for cost tracking
```

### 4. API Key Compromise
```bash
# 1. Immediately revoke key in OpenAI dashboard
# 2. Update .env file with new key
# 3. Restart any running processes
# 4. Audit recent usage for unauthorized access
```

## 🧹 Maintenance Tasks

### Weekly Maintenance
1. **Clean Orphaned Embeddings**
   ```bash
   python3 scripts/vectorstore_health_check.py --fix
   ```

2. **Verify Backup Integrity**
   ```bash
   python3 scripts/backup_vectorstore.py --verify latest
   ```

3. **Check Storage Usage**
   ```bash
   du -sh vectorstore/
   ls -la backups/
   ```

### Monthly Maintenance
1. **Full Re-verification**
   ```bash
   python3 scripts/vectorstore_health_check.py --deep-scan
   ```

2. **Cleanup Old Backups**
   ```bash
   # Keep last 30 days
   find backups/ -name "*.tar.gz" -mtime +30 -delete
   ```

3. **Performance Audit**
   ```bash
   # Review logs for performance trends
   grep "Processing rate" logs/daily_update.log | tail -30
   ```

## 📈 Scaling Considerations

### When to Scale
- Processing time > 4 hours
- Memory usage consistently > 80%
- Storage approaching disk limits
- API rate limits frequently hit

### Scaling Options
1. **Horizontal**: Process frameworks in parallel
2. **Vertical**: Increase memory/CPU for larger batches
3. **Storage**: Move to networked storage solution
4. **API**: Upgrade OpenAI tier for higher limits

## 🎯 Optimization Tips

1. **Memory Management**
   - Process frameworks separately
   - Clear collections between large batches
   - Monitor vectorstore size

2. **Performance Tuning**
   - Adjust batch size based on document size
   - Use framework-specific collections for faster queries
   - Enable where-clause filtering when possible

3. **Storage Efficiency**
   - Regular cleanup of orphaned embeddings
   - Compress backup files
   - Monitor chunk distribution

4. **RAG Query Optimization**
   - Use framework filtering when possible
   - Expand queries for better coverage
   - Cache common query results (optional)

## 🐛 Common Issues and Solutions

### "Dimension Mismatch" Error
**Cause**: Mixing ChromaDB default with OpenAI embeddings  
**Solution**: Always specify OpenAI embedding function

### "Collection Name Invalid" Error
**Cause**: Framework name with special characters  
**Solution**: Use `validate_collection_name()` function

### "Rate Limit Exceeded" Error
**Cause**: Too many OpenAI API requests  
**Solution**: Reduce batch size or increase delays

### "Checkpoint Resume Failed"
**Cause**: Corrupted checkpoint file  
**Solution**: Delete checkpoint and restart (safe with hash tracking)

### Slow Processing
**Check**: Network latency to OpenAI  
**Solution**: Increase batch size, reduce rate limit delays

### High Memory Usage
**Check**: Batch size and concurrent operations  
**Solution**: Reduce batch size, process frameworks separately

### Inconsistent Search Results
**Check**: Embedding function consistency  
**Solution**: Re-embed affected collections with correct function

## 📝 Operational Runbook

### Daily Operations Checklist
- [ ] Check health monitoring dashboard
- [ ] Verify overnight update completed
- [ ] Review error logs
- [ ] Check storage usage
- [ ] Validate backup created

### Weekly Operations Checklist
- [ ] Run full health check with fixes
- [ ] Verify backup integrity
- [ ] Clean up old logs
- [ ] Review cost tracking
- [ ] Update documentation if needed

### Incident Response Plan
1. **Identify**: Check monitoring alerts
2. **Assess**: Determine scope and impact
3. **Respond**: Follow emergency procedures
4. **Recover**: Restore from backup if needed
5. **Review**: Document lessons learned

## 💰 Cost Analysis

### One-Time Costs
- **Initial Embedding**: ~$6.44 (323,118 embeddings)
- **Average per document**: $0.00002

### Ongoing Costs
- **Daily Updates**: <$0.50 (typical)
- **Monthly Estimate**: $10-15
- **Annual Projection**: $120-180

### Cost Optimization
- Process only changed files (ETag/hash detection)
- Batch operations efficiently
- Monitor cost per framework
- Set appropriate cost limits