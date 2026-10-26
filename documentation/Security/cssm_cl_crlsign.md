# CSSM_CL_CrlSign

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CrlSign(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const SecAsn1Item *UnsignedCrl, const CSSM_FIELD *SignScope, uint32 ScopeSize, CSSM_DATA_PTR SignedCrl);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_crlsign)*