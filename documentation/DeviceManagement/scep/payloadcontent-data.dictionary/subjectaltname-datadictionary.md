# SCEP.PayloadContent.SubjectAltName

**Framework**: Device Management  
**Kind**: dictionary

An optional dictionary that provides values required by the CA for issuing a certificate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SCEP.PayloadContent.SubjectAltName
```

## Properties

- `dNSName` (string): The DNS name.
- `ntPrincipalName` (string): The NT principal name. Use an other name OID set to `1.3.6.1.4.1.311.20.2.3`.
- `rfc822Name` (string): The RFC 822 (email address) string.
- `uniformResourceIdentifier` (string): The Uniform Resource Identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scep/payloadcontent-data.dictionary/subjectaltname-data.dictionary)*