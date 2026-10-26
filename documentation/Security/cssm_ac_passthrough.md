# CSSM_AC_PassThrough

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_AC_PassThrough(CSSM_AC_HANDLE ACHandle, CSSM_TP_HANDLE TPHandle, CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_DL_DB_LIST *DBList, uint32 PassThroughId, const void *InputParams, void **OutputParams);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_ac_passthrough)*