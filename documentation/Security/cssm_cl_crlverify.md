# CSSM_CL_CrlVerify

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CrlVerify(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *CrlToBeVerified, const SecAsn1Item *SignerCert, const CSSM_FIELD *VerifyScope, uint32 ScopeSize);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_crlverify)*