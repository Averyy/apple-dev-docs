# CSSM_CL_CrlAddCert

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CrlAddCert(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *Cert, uint32 NumberOfFields, const CSSM_FIELD *CrlEntryFields, const SecAsn1Item *OldCrl, CSSM_DATA_PTR NewCrl);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_crladdcert)*