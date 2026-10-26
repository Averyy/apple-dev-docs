# CSSM_EncryptDataUpdate

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_EncryptDataUpdate(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *ClearBufs, uint32 ClearBufCount, CSSM_DATA_PTR CipherBufs, uint32 CipherBufCount, CSSM_SIZE *bytesEncrypted);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_encryptdataupdate)*