# CSSM_VerifyData

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_VerifyData(CSSM_CC_HANDLE CCHandle, const SecAsn1Item *DataBufs, uint32 DataBufCount, CSSM_ALGORITHMS DigestAlgorithm, const SecAsn1Item *Signature);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_verifydata)*