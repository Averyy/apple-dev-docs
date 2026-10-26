# CSSM_CSP_CreateKeyGenContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CSP_CreateKeyGenContext(CSSM_CSP_HANDLE CSPHandle, CSSM_ALGORITHMS AlgorithmID, uint32 KeySizeInBits, const CSSM_CRYPTO_DATA *Seed, const SecAsn1Item *Salt, const CSSM_DATE *StartDate, const CSSM_DATE *EndDate, const SecAsn1Item *Params, CSSM_CC_HANDLE *NewContextHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_csp_createkeygencontext)*