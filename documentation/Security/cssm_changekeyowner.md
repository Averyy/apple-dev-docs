# CSSM_ChangeKeyOwner

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_ChangeKeyOwner(CSSM_CSP_HANDLE CSPHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const CSSM_ACL_OWNER_PROTOTYPE *NewOwner);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_changekeyowner)*