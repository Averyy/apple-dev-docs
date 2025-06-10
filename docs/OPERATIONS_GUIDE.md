# Operations Guide

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

## 🔄 Incremental Updates

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

## 🔍 Troubleshooting Guide

### Common Issues

**Slow Processing**
- Check: Network latency to OpenAI
- Solution: Increase batch size, reduce rate limit delays

**High Memory Usage**
- Check: Batch size and concurrent operations
- Solution: Reduce batch size, process frameworks separately

**Checkpoint Recovery Fails**
- Check: Checkpoint file corruption
- Solution: Delete checkpoint, rely on hash-based detection

**Inconsistent Search Results**
- Check: Embedding function consistency
- Solution: Re-embed affected collections with correct function

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