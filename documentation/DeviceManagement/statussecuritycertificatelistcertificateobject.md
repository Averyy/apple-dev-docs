# StatusSecurityCertificateListCertificateObject

**Framework**: Device Management  
**Kind**: dictionary

A status report of a security certificate.

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
object StatusSecurityCertificateListCertificateObject
```

## Properties

- `_removed` (boolean): If `true`, the system removed the app and only this key and the `identifier` key are present in the status item object.
- `data` (string) *(required)*: The certificate data in DER-encoded X.509 format.
- `declaration-identifier` (string): The identifier of the asset declaration that installed the certificate, which is only present if a declaration installed the certificate.
- `identifier` (string) *(required)*: The unique identifier of the certificate which the system uses as the primary key.
- `is-identity` (boolean) *(required)*: If `true`, the certificate is an identity certificate.
- `subject-summary` (string) *(required)*: The summary of the certificate’s subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussecuritycertificatelistcertificateobject)*