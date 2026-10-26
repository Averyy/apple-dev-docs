# CSSM_TP_FormSubmit

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_FormSubmit(CSSM_TP_HANDLE TPHandle, CSSM_TP_FORM_TYPE FormType, const SecAsn1Item *Form, const CSSM_TP_AUTHORITY_ID *ClearanceAuthority, const CSSM_TP_AUTHORITY_ID *RepresentedAuthority, CSSM_ACCESS_CREDENTIALS_PTR Credentials);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_formsubmit)*