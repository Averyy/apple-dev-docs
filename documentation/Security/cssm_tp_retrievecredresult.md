# CSSM_TP_RetrieveCredResult

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_RetrieveCredResult(CSSM_TP_HANDLE TPHandle, const SecAsn1Item *ReferenceIdentifier, const CSSM_TP_CALLERAUTH_CONTEXT *CallerAuthCredentials, sint32 *EstimatedTime, CSSM_BOOL *ConfirmationRequired, CSSM_TP_RESULT_SET_PTR*RetrieveOutput);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_retrievecredresult)*