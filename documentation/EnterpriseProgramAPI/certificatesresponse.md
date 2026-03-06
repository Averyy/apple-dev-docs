# CertificatesResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary

A response that contains a list of Certificates resources.

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

- [object Certificate](certificate.md)
  The data structure that represents a Certificates resource.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response that contains a single certificate resource without includes.
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificateResponse](certificateresponse.md)
  A response that contains a single Certificates resource.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/certificatesresponse)*