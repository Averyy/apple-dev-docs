# CSSM_TP_CrlSign

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_CrlSign(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_ENCODED_CRL *CrlToBeSigned, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *SignerVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR SignerVerifyResult, CSSM_DATA_PTR SignedCrl);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_crlsign)*