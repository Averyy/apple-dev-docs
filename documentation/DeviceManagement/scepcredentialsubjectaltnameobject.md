# SCEPCredentialSubjectAltNameObject

**Framework**: Device Management  
**Kind**: dictionary

The subject’s alternative name for the certificate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SCEPCredentialSubjectAltNameObject
```

## Properties

- `dNSName` (string): The DNS name.
- `ntPrincipalName` (string): The NT principal name. Use an other name OID set to `1.3.6.1.4.1.311.20.2.3`.
- `rfc822Name` (string): The RFC 822 email address.
- `uniformResourceIdentifier` (string): The uniform resource identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scepcredentialsubjectaltnameobject)*