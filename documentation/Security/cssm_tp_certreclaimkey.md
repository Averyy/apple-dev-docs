# CSSM_TP_CertReclaimKey

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_CertReclaimKey(CSSM_TP_HANDLE TPHandle, const CSSM_CERTGROUP *CertGroup, uint32 CertIndex, CSSM_LONG_HANDLE KeyCacheHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_certreclaimkey)*