# CSSM_DecryptData

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_DecryptData(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *CipherBufs, uint32 CipherBufCount, CSSM_DATA_PTR ClearBufs, uint32 ClearBufCount, CSSM_SIZE *bytesDecrypted, CSSM_DATA_PTR RemData);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_decryptdata)*