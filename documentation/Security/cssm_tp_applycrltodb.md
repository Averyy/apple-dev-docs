# CSSM_TP_ApplyCrlToDb

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_ApplyCrlToDb(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_ENCODED_CRL *CrlToBeApplied, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *ApplyCrlVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR ApplyCrlVerifyResult);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_applycrltodb)*