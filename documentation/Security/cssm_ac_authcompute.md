# CSSM_AC_AuthCompute

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_AC_AuthCompute(CSSM_AC_HANDLE ACHandle, const CSSM_TUPLEGROUP *BaseAuthorizations, const CSSM_TUPLEGROUP *Credentials, uint32 NumberOfRequestors, const CSSM_LIST *Requestors, const CSSM_LIST *RequestedAuthorizationPeriod, const CSSM_LIST *RequestedAuthorization, CSSM_TUPLEGROUP_PTR AuthorizationResult);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_ac_authcompute)*