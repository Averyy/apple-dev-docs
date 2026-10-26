# CSSM_TP_ConfirmCredResult

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_ConfirmCredResult(CSSM_TP_HANDLE TPHandle, const SecAsn1Item *ReferenceIdentifier, const CSSM_TP_CALLERAUTH_CONTEXT *CallerAuthCredentials, const CSSM_TP_CONFIRM_RESPONSE *Responses, const CSSM_TP_AUTHORITY_ID *PreferredAuthority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_confirmcredresult)*