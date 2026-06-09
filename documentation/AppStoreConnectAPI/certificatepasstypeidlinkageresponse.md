# CertificatePassTypeIdLinkageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response body that contains the ID of a single related resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object CertificatePassTypeIdLinkageResponse
```

## Topics

### Dictionaries
- [object CertificatePassTypeIdLinkageResponse.Data](certificatepasstypeidlinkageresponse/data-data.dictionary.md)
  The resource linkage data identifying the pass type ID associated with a certificate.

## Properties

- `data` (CertificatePassTypeIdLinkageResponse.Data) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

- [object Certificate](certificate.md)
  A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response containing a list of certificates, without related resources.
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificateResponse](certificateresponse.md)
  The response body for endpoints that create or read a single signing certificate.
- [object CertificatesResponse](certificatesresponse.md)
  The response body for endpoints that list signing certificates.
- [object CertificateUpdateRequest](certificateupdaterequest.md)
  The request body you use to update a certificate activation status.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificatepasstypeidlinkageresponse)*