# CertificateTransparency.SubjectPublicKeyInfoHashDict

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of hashed public keys.

**Availability**:
- iOS 12.1.1+
- iPadOS 12.1.1+
- macOS 10.14.2+
- tvOS 12.1.1+
- visionOS 1.0+
- watchOS 5.1.1+

## Declaration

```swift
object CertificateTransparency.SubjectPublicKeyInfoHashDict
```

## Properties

- `Algorithm` (string) *(required)*: The algorithm must be `sha256`.
- `Hash` (data) *(required)*: The hash of the DER-encoding of the certificate’s `subjectPublicKeyInfo`. The hash field requires the data (`subjectPublicKeyInfo` hash) in a specific format: a Base64 encoded (binary) SHA-256 hash of the certificate’s public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatetransparency/subjectpublickeyinfohashdict)*