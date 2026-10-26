# CSSM_TP_SubmitCredRequest

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_SubmitCredRequest(CSSM_TP_HANDLE TPHandle, const CSSM_TP_AUTHORITY_ID *PreferredAuthority, CSSM_TP_AUTHORITY_REQUEST_TYPE RequestType, const CSSM_TP_REQUEST_SET *RequestInput, const CSSM_TP_CALLERAUTH_CONTEXT *CallerAuthContext, sint32 *EstimatedTime, CSSM_DATA_PTR ReferenceIdentifier);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_submitcredrequest)*