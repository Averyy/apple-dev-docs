# VerificationResult.VerificationError.invalidSignature

**Framework**: StoreKit  
**Kind**: case

An error that indicates that the signature didn’t match the header and payload.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case invalidSignature
```

## See Also

- [VerificationResult.VerificationError.invalidCertificateChain](verificationresult/verificationerror/invalidcertificatechain.md)
  An error indicating that the certificate chain is invalid.
- [VerificationResult.VerificationError.invalidDeviceVerification](verificationresult/verificationerror/invaliddeviceverification.md)
  An error that indicates the signed value wasn’t generated for the current device.
- [VerificationResult.VerificationError.invalidEncoding](verificationresult/verificationerror/invalidencoding.md)
  An error that indicates the signature, certificate chain, or other part of value uses invalid encoding.
- [VerificationResult.VerificationError.missingRequiredProperties](verificationresult/verificationerror/missingrequiredproperties.md)
  An error that indicates the header or payload are missing information that’s required to verify the signature.
- [VerificationResult.VerificationError.revokedCertificate](verificationresult/verificationerror/revokedcertificate.md)
  An error that indicates the certificate chain includes a revoked certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/verificationerror/invalidsignature)*