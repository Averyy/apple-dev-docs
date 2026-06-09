# CertificatesWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of certificates, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object CertificatesWithoutIncludesResponse
```

## Properties

- `data` ([Certificate]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object Certificate](certificate.md)
  A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.
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
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificateswithoutincludesresponse)*