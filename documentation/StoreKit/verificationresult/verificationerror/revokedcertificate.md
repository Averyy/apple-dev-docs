# VerificationResult.VerificationError.revokedCertificate

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

An error that indicates the certificate chain includes a revoked certificate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case revokedCertificate
```

## Discussion

In some cases, this error may resolve if you try again later.

## See Also

### Error Codes
- [VerificationResult.VerificationError.invalidCertificateChain](./invalidcertificatechain.md)
  An error indicating that the certificate chain is invalid.
- [VerificationResult.VerificationError.invalidDeviceVerification](./invaliddeviceverification.md)
  An error that indicates the signed value wasn’t generated for the current device.
- [VerificationResult.VerificationError.invalidEncoding](./invalidencoding.md)
  An error that indicates the signature, certificate chain, or other part of value uses invalid encoding.
- [VerificationResult.VerificationError.invalidSignature](./invalidsignature.md)
  An error that indicates that the signature didn’t match the header and payload.
- [VerificationResult.VerificationError.missingRequiredProperties](./missingrequiredproperties.md)
  An error that indicates the header or payload are missing information that’s required to verify the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/verificationerror/revokedcertificate)*