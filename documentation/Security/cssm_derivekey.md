# CSSM_DeriveKey

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_DeriveKey(CSSM_CC_HANDLE CCHandle, CSSM_DATA_PTR Param, uint32 KeyUsage, uint32 KeyAttr, const SecAsn1Item *KeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR DerivedKey);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_derivekey)*