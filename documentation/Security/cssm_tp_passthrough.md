# CSSM_TP_PassThrough

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_TP_PassThrough(CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_DL_DB_LIST *DBList, uint32 PassThroughId, const void *InputParams, void **OutputParams);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_tp_passthrough)*