# CSSM_GenerateKeyPairP

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_GenerateKeyPairP(CSSM_CC_HANDLE CCHandle, uint32 PublicKeyUsage, uint32 PublicKeyAttr, const SecAsn1Item *PublicKeyLabel, CSSM_KEY_PTR PublicKey, uint32 PrivateKeyUsage, uint32 PrivateKeyAttr, const SecAsn1Item *PrivateKeyLabel, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, CSSM_KEY_PTR PrivateKey, CSSM_PRIVILEGE Privilege);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_generatekeypairp)*