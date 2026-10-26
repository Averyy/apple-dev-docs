# CSSM_TP_CertRevoke

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_CertRevoke(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CSP_HANDLE CSPHandle, const SecAsn1Item *OldCrlTemplate, const CSSM_CERTGROUP *CertGroupToBeRevoked, const CSSM_CERTGROUP *RevokerCertGroup, const CSSM_TP_VERIFY_CONTEXT *RevokerVerifyContext, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR RevokerVerifyResult, CSSM_TP_CERTCHANGE_REASON Reason, CSSM_DATA_PTR NewCrlTemplate);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_certrevoke)*