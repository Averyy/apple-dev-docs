# CertificatesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list signing certificates.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object CertificatesResponse
```

## Properties

- `data` ([Certificate]) *(required)*: The resource data.
- `included` ([PassTypeId])
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information

## See Also

- [List and download certificates](get-v1-certificates.md)
  Find and list certificates and download their data.
- [object Certificate](certificate.md)
  A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response containing a list of certificates, without related resources.
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificateResponse](certificateresponse.md)
  The response body for endpoints that create or read a single signing certificate.
- [object CertificateUpdateRequest](certificateupdaterequest.md)
  The request body you use to update a certificate activation status.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificatesresponse)*