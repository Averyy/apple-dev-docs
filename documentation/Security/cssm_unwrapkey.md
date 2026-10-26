# CSSM_UnwrapKey

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_UnwrapKey(CSSM_CC_HANDLE CCHandle, const CSSM_KEY *PublicKey, const CSSM_WRAP_KEY *WrappedKey, uint32 KeyUsage, uint32 KeyAttr, const SecAsn1Item *KeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR UnwrappedKey, CSSM_DATA_PTR DescriptiveData);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_unwrapkey)*