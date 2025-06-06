# VerificationResult.VerificationError

**Framework**: StoreKit  
**Kind**: enum

Error cases for StoreKit JWS verification.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum VerificationError
```

## Topics

### Error Codes
- [VerificationResult.VerificationError.invalidCertificateChain](verificationresult/verificationerror/invalidcertificatechain.md)
  An error indicating that the certificate chain is invalid.
- [VerificationResult.VerificationError.invalidDeviceVerification](verificationresult/verificationerror/invaliddeviceverification.md)
  An error that indicates the signed value wasn’t generated for the current device.
- [VerificationResult.VerificationError.invalidEncoding](verificationresult/verificationerror/invalidencoding.md)
  An error that indicates the signature, certificate chain, or other part of value uses invalid encoding.
- [VerificationResult.VerificationError.invalidSignature](verificationresult/verificationerror/invalidsignature.md)
  An error that indicates that the signature didn’t match the header and payload.
- [VerificationResult.VerificationError.missingRequiredProperties](verificationresult/verificationerror/missingrequiredproperties.md)
  An error that indicates the header or payload are missing information that’s required to verify the signature.
- [VerificationResult.VerificationError.revokedCertificate](verificationresult/verificationerror/revokedcertificate.md)
  An error that indicates the certificate chain includes a revoked certificate.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum VerificationResult](verificationresult.md)
  A type that describes the result of a StoreKit verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verificationresult/verificationerror)*