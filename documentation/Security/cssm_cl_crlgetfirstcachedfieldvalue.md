# CSSM_CL_CrlGetFirstCachedFieldValue

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CrlGetFirstCachedFieldValue(CSSM_CL_HANDLE CLHandle, CSSM_HANDLE CrlHandle, const SecAsn1Item *CrlRecordIndex, const SecAsn1Oid *CrlField, CSSM_HANDLE_PTR ResultsHandle, uint32 *NumberOfMatchedFields, CSSM_DATA_PTR*Value);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_crlgetfirstcachedfieldvalue)*