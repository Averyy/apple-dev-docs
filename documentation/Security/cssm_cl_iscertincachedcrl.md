# CSSM_CL_IsCertInCachedCrl

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_IsCertInCachedCrl(CSSM_CL_HANDLE CLHandle, const SecAsn1Item *Cert, CSSM_HANDLE CrlHandle, CSSM_BOOL *CertFound, CSSM_DATA_PTR CrlRecordIndex);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_iscertincachedcrl)*