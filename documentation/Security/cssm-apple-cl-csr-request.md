# CSSM_APPLE_CL_CSR_REQUEST

**Framework**: Security  
**Kind**: struct

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CSSM_APPLE_CL_CSR_REQUEST
```

## Topics

### Initializers
- [init()](cssm_apple_cl_csr_request/init.md)
- [init(subjectNameX509: UnsafeMutablePointer<cssm_x509_name>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: SecAsn1Oid, cspHand: CSSM_CSP_HANDLE, subjectPublicKey: UnsafePointer<cssm_key>!, subjectPrivateKey: UnsafePointer<cssm_key>!, challengeString: UnsafePointer<CChar>!)](cssm_apple_cl_csr_request/init(subjectnamex509:signaturealg:signatureoid:csphand:subjectpublickey:subjectprivatekey:challengestring:).md)
### Instance Properties
- [var challengeString: UnsafePointer<CChar>!](cssm_apple_cl_csr_request/challengestring.md)
- [var cspHand: CSSM_CSP_HANDLE](cssm_apple_cl_csr_request/csphand.md)
- [var signatureAlg: CSSM_ALGORITHMS](cssm_apple_cl_csr_request/signaturealg.md)
- [var signatureOid: SecAsn1Oid](cssm_apple_cl_csr_request/signatureoid.md)
- [var subjectNameX509: UnsafeMutablePointer<cssm_x509_name>!](cssm_apple_cl_csr_request/subjectnamex509.md)
- [var subjectPrivateKey: UnsafePointer<cssm_key>!](cssm_apple_cl_csr_request/subjectprivatekey.md)
- [var subjectPublicKey: UnsafePointer<cssm_key>!](cssm_apple_cl_csr_request/subjectpublickey.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_apple_cl_csr_request)*