# CSSM_CL_CrlSetFields

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CrlSetFields(CSSM_CL_HANDLE CLHandle, uint32 NumberOfFields, const CSSM_FIELD *CrlTemplate, const SecAsn1Item *OldCrl, CSSM_DATA_PTR ModifiedCrl);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_crlsetfields)*