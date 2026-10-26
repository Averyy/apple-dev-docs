# CSSM_TP_CertSign

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_CertSign(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *CertTemplateToBeSigned, const CSSM_CERTGROUP *SignerCertGroup, const CSSM_TP_VERIFY_CONTEXT *SignerVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR SignerVerifyResult, CSSM_DATA_PTR SignedCert);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_certsign)*