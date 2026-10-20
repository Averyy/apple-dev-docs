# CertificateListResponse.CertificateListItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains information about a certificate list item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object CertificateListResponse.CertificateListItem
```

## Properties

- `CommonName` (string) *(required)*: The certificate’s common name.
- `Data` (data) *(required)*: The certificate in DER-encoded X.509 format.
- `IsIdentity` (boolean) *(required)*: If `true`, this is an identity certificate.

## See Also

### Objects
- [object CertificateListResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatelistresponse/certificatelistitem)*