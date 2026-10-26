# CSSM_CL_CertGroupFromVerifiedBundle

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_CL_CertGroupFromVerifiedBundle(CSSM_CL_HANDLE CLHandle, CSSM_CC_HANDLE CCHandle, const CSSM_CERT_BUNDLE *CertBundle, const SecAsn1Item *SignerCert, CSSM_CERTGROUP_PTR*CertGroup);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_cl_certgroupfromverifiedbundle)*