# CertificateRevocation.SubjectPublicKeyInfoHashDict

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of hashed public keys.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- visionOS 1.1+

## Declaration

```swift
object CertificateRevocation.SubjectPublicKeyInfoHashDict
```

## Properties

- `Algorithm` (string) *(required)*: The algorithm must be `sha256`.
- `Hash` (data) *(required)*: The hash of the DER-encoding of the certificate’s `subjectPublicKeyInfo`. The hash field requires the data (`subjectPublicKeyInfo` hash) in a specific format: a Base64 encoded (binary) SHA-256 hash of the certificate’s public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificaterevocation/subjectpublickeyinfohashdict)*