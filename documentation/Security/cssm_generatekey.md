# CSSM_GenerateKey

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_GenerateKey(CSSM_CC_HANDLE CCHandle, uint32 KeyUsage, uint32 KeyAttr, const SecAsn1Item *KeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR Key);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_generatekey)*