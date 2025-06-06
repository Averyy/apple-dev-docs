# CSSM_APPLE_TP_CERT_REQUEST

**Framework**: Security  
**Kind**: struct

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CSSM_APPLE_TP_CERT_REQUEST
```

## Topics

### Initializers
- [init()](cssm_apple_tp_cert_request/init.md)
- [init(cspHand: CSSM_CSP_HANDLE, clHand: CSSM_CL_HANDLE, serialNumber: uint32, numSubjectNames: uint32, subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, numIssuerNames: uint32, issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!, certPublicKey: UnsafePointer<cssm_key>!, issuerPrivateKey: UnsafePointer<cssm_key>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: SecAsn1Oid, notBefore: uint32, notAfter: uint32, numExtensions: uint32, extensions: UnsafeMutablePointer<__CE_DataAndType>!, challengeString: UnsafePointer<CChar>!)](cssm_apple_tp_cert_request/init(csphand:clhand:serialnumber:numsubjectnames:subjectnames:numissuernames:issuernames:issuernamex509:certpublickey:issuerprivatekey:signaturealg:signatureoid:notbefore:notafter:numextensions:extensions:challengestring:).md)
### Instance Properties
- [var certPublicKey: UnsafePointer<cssm_key>!](cssm_apple_tp_cert_request/certpublickey.md)
- [var challengeString: UnsafePointer<CChar>!](cssm_apple_tp_cert_request/challengestring.md)
- [var clHand: CSSM_CL_HANDLE](cssm_apple_tp_cert_request/clhand.md)
- [var cspHand: CSSM_CSP_HANDLE](cssm_apple_tp_cert_request/csphand.md)
- [var extensions: UnsafeMutablePointer<__CE_DataAndType>!](cssm_apple_tp_cert_request/extensions.md)
- [var issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!](cssm_apple_tp_cert_request/issuernamex509.md)
- [var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!](cssm_apple_tp_cert_request/issuernames.md)
- [var issuerPrivateKey: UnsafePointer<cssm_key>!](cssm_apple_tp_cert_request/issuerprivatekey.md)
- [var notAfter: uint32](cssm_apple_tp_cert_request/notafter.md)
- [var notBefore: uint32](cssm_apple_tp_cert_request/notbefore.md)
- [var numExtensions: uint32](cssm_apple_tp_cert_request/numextensions.md)
- [var numIssuerNames: uint32](cssm_apple_tp_cert_request/numissuernames.md)
- [var numSubjectNames: uint32](cssm_apple_tp_cert_request/numsubjectnames.md)
- [var serialNumber: uint32](cssm_apple_tp_cert_request/serialnumber.md)
- [var signatureAlg: CSSM_ALGORITHMS](cssm_apple_tp_cert_request/signaturealg.md)
- [var signatureOid: SecAsn1Oid](cssm_apple_tp_cert_request/signatureoid.md)
- [var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!](cssm_apple_tp_cert_request/subjectnames.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_apple_tp_cert_request)*