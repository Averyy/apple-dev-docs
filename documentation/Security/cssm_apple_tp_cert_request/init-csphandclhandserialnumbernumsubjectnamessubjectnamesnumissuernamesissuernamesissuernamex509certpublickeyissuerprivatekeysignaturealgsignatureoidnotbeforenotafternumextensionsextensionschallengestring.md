# init(cspHand:clHand:serialNumber:numSubjectNames:subjectNames:numIssuerNames:issuerNames:issuerNameX509:certPublicKey:issuerPrivateKey:signatureAlg:signatureOid:notBefore:notAfter:numExtensions:extensions:challengeString:)

**Framework**: Security  
**Kind**: init

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(cspHand: CSSM_CSP_HANDLE, clHand: CSSM_CL_HANDLE, serialNumber: uint32, numSubjectNames: uint32, subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, numIssuerNames: uint32, issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!, certPublicKey: UnsafePointer<cssm_key>!, issuerPrivateKey: UnsafePointer<cssm_key>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: SecAsn1Oid, notBefore: uint32, notAfter: uint32, numExtensions: uint32, extensions: UnsafeMutablePointer<__CE_DataAndType>!, challengeString: UnsafePointer<CChar>!)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_apple_tp_cert_request/init(csphand:clhand:serialnumber:numsubjectnames:subjectnames:numissuernames:issuernames:issuernamex509:certpublickey:issuerprivatekey:signaturealg:signatureoid:notbefore:notafter:numextensions:extensions:challengestring:))*