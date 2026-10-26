# CSSM_CSP_CreateDeriveKeyContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CSP_CreateDeriveKeyContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, CSSM_KEY_TYPE DeriveKeyType, uint32 DeriveKeyLengthInBits, const CSSM_ACCESS_CREDENTIALS *AccessCred, const CSSM_KEY *BaseKey, uint32 IterationCount, const SecAsn1Item *Salt, const CSSM_CRYPTO_DATA *Seed, CSSM_CC_HANDLE *NewContextHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_csp_createderivekeycontext)*