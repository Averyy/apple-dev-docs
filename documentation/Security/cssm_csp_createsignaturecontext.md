# CSSM_CSP_CreateSignatureContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CSP_CreateSignatureContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *Key, CSSM_CC_HANDLE *NewContextHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_csp_createsignaturecontext)*