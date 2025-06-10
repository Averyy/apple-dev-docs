# Security Guide

## 🔐 API Key Management

### Critical Security Rules

**✅ DO:**
- Store API keys in environment variables only
- Use `.env` files (gitignored) for local development
- Rotate keys regularly (recommended: every 90 days)
- Restrict API key permissions when possible
- Monitor API usage for anomalies

**❌ DON'T:**
- Hardcode API keys in source code
- Commit `.env` files to version control
- Share API keys via email or chat
- Use production keys in development
- Leave unrestricted keys active

### Secure Configuration

```bash
# .env file (NEVER commit this)
OPENAI_API_KEY="sk-..."
MAX_EMBEDDING_COST="10.00"

# Environment validation in code
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable must be set")
```

### OpenAI API Key Restrictions
1. Login to OpenAI dashboard
2. Create new restricted key
3. Set permissions:
   - ✅ Models: Read
   - ✅ Model capabilities: Write (for embeddings)
   - ❌ Fine-tuning: None
   - ❌ Assistants: None
   - ❌ Administration: None
4. Set usage limits:
   - Monthly budget: $50
   - Rate limits: 3000 RPM

## 💰 Cost Protection Mechanisms

### Multiple Safety Layers

1. **Hard Cost Limit**
   ```python
   MAX_COST_LIMIT = float(os.getenv("MAX_EMBEDDING_COST", "10.00"))
   ```

2. **User Confirmation**
   - Automatic prompt for costs > $0.01
   - Requires explicit "yes" to proceed

3. **Real-Time Tracking**
   - Cost calculated before each batch
   - Immediate abort if limit exceeded
   - Running total displayed during processing

4. **Batch-Level Protection**
   ```python
   if actual_cost + batch_cost > MAX_COST_LIMIT:
       logger.error("Stopping: Next batch would exceed cost limit")
       break
   ```

### Cost Monitoring
```bash
# Check current month's usage
curl https://api.openai.com/v1/usage \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Monitor embedding costs in logs
grep "Actual cost:" logs/embedding.log | tail -20
```

## 🛡️ Input Validation

### Path Traversal Protection
```python
# Validate framework names
if not re.match(r'^[a-zA-Z0-9_-]+$', framework):
    raise ValueError(f"Invalid framework name: {framework}")

# Sanitize file paths
safe_path = Path(base_dir) / Path(user_input).name
```

### File Size Limits
```python
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
if file_path.stat().st_size > MAX_FILE_SIZE:
    logger.warning(f"Skipping large file: {file_path}")
```

### Collection Name Sanitization
```python
def validate_collection_name(name: str) -> str:
    # ChromaDB requirements
    if len(name) < 3 or len(name) > 63:
        raise ValueError("Collection name must be 3-63 characters")
    
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$', name):
        raise ValueError("Invalid collection name format")
    
    return name
```

## 🔒 Access Control

### File System Permissions
```bash
# Secure sensitive files
chmod 600 .env
chmod 600 mcp-server/.env

# Protect configuration
chmod 644 pyproject.toml
chmod 755 scripts/*.py

# Secure backups
chmod 600 backups/*.tar.gz
```

### Directory Structure
```bash
# Recommended permissions
drwxr-xr-x  documentation/  # Read-only scraped docs
drwx------  .hashes/        # Protected hash storage
drwx------  vectorstore/    # Protected embeddings
drwx------  backups/        # Protected backups
```

## 🚨 Security Monitoring

### Audit Logging
All security-relevant events are logged:
- API key validation failures
- Cost limit exceeded events
- Invalid input attempts
- Unauthorized access attempts

### Log Review
```bash
# Check for security issues
grep -E "ERROR|CRITICAL|Unauthorized|Invalid" logs/*.log

# Monitor API key usage
grep "API key" logs/security.log | tail -50
```

### Anomaly Detection
Monitor for:
- Sudden spike in API costs
- Unusual processing patterns
- Failed authentication attempts
- Unexpected file access patterns

## 🔑 Emergency Response

### API Key Compromise

**Immediate Actions:**
1. Revoke compromised key in OpenAI dashboard
2. Generate new restricted key
3. Update all `.env` files
4. Restart all services
5. Audit recent API usage

**Post-Incident:**
1. Review how compromise occurred
2. Strengthen key management practices
3. Enable additional monitoring
4. Document lessons learned

### Data Breach Response

**If vector store exposed:**
1. Assess scope of exposure
2. Rotate all API keys
3. Rebuild vector store from scratch
4. Notify stakeholders if needed
5. Review and strengthen access controls

## ✅ Security Checklist

### Pre-Deployment
- [ ] API keys in environment variables only
- [ ] `.env` files in `.gitignore`
- [ ] Cost limits configured
- [ ] Input validation active
- [ ] File permissions set correctly

### Operational Security
- [ ] Regular key rotation schedule
- [ ] Monthly cost review
- [ ] Security log monitoring
- [ ] Backup encryption enabled
- [ ] Access logging configured

### Incident Preparedness
- [ ] Emergency contacts documented
- [ ] Key revocation process tested
- [ ] Backup restoration verified
- [ ] Incident response plan reviewed
- [ ] Team security training completed

## 🎯 Best Practices

1. **Principle of Least Privilege**
   - Use restricted API keys
   - Limit file system access
   - Minimize exposed endpoints

2. **Defense in Depth**
   - Multiple cost control layers
   - Input validation at every level
   - Comprehensive error handling

3. **Security by Design**
   - Secure defaults in configuration
   - Fail-safe rather than fail-open
   - Clear security documentation

4. **Continuous Improvement**
   - Regular security reviews
   - Stay updated on vulnerabilities
   - Learn from incidents

## 📚 Additional Resources

- [OpenAI API Security Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)
- [ChromaDB Security Considerations](https://docs.trychroma.com/production)
- [Python Security Guidelines](https://python.readthedocs.io/en/latest/library/security_warnings.html)