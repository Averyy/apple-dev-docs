# CSSM_TP_CrlVerify

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_CrlVerify(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const CSSM_ENCODED_CRL *CrlToBeVerified, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *VerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR RevokerVerifyResult);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_crlverify)*