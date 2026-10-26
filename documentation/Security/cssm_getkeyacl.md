# CSSM_GetKeyAcl

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_GetKeyAcl(CSSM_CSP_HANDLE CSPHandle, const CSSM_KEY *Key, const CSSM_STRING *SelectionTag, uint32 *NumberOfAclInfos, CSSM_ACL_ENTRY_INFO_PTR*AclInfos);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_getkeyacl)*