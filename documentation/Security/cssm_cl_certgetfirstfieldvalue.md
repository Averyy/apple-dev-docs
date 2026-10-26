# CSSM_CL_CertGetFirstFieldValue

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CertGetFirstFieldValue(CSSM_CL_HANDLE CLHandle, const SecAsn1Item *Cert, const SecAsn1Oid *CertField, CSSM_HANDLE_PTR ResultsHandle, uint32 *NumberOfMatchedFields, CSSM_DATA_PTR*Value);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_certgetfirstfieldvalue)*