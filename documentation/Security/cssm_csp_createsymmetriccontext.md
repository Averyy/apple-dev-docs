# CSSM_CSP_CreateSymmetricContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CSP_CreateSymmetricContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, CSSM_ENCRYPT_MODE Mode, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, const SecAsn1Item *InitVector, CSSM_PADDING Padding, void *Reserved, CSSM_CC_HANDLE *NewContextHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_csp_createsymmetriccontext)*