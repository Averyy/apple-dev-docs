# CSSM_CSP_CreateRandomGenContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CSP_CreateRandomGenContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, const CSSM_CRYPTO_DATA *Seed, CSSM_SIZE Length, CSSM_CC_HANDLE *NewContextHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_csp_createrandomgencontext)*