# CSSM_WrapKeyP

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_WrapKeyP(CSSM_CC_HANDLE CCHandle, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const SecAsn1Item *DescriptiveData, CSSM_WRAP_KEY_PTR WrappedKey, CSSM_PRIVILEGE Privilege);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_wrapkeyp)*