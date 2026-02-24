# ACMECredentialSubjectAltNameObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies the subject’s alternative name that the device requests for the certificate that the ACME server issues.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ACMECredentialSubjectAltNameObject
```

## Properties

- `dNSName` (string): The DNS name.
- `ntPrincipalName` (string): The NT principal name. Use an other name OID set to `1.3.6.1.4.1.311.20.2.3`.
- `rfc822Name` (string): The RFC 822 email address.
- `uniformResourceIdentifier` (string): The uniform resource identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/acmecredentialsubjectaltnameobject)*