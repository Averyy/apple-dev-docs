# CertificateResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create or read a single signing certificate.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object CertificateResponse
```

## Properties

- `data` (Certificate) *(required)*: The resource data.
- `included` ([PassTypeId])
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [Create a certificate](post-v1-certificates.md)
  Create a new certificate using a certificate signing request.
- [object Certificate](certificate.md)
  A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response containing a list of certificates, without related resources.
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificatesResponse](certificatesresponse.md)
  The response body for endpoints that list signing certificates.
- [object CertificateUpdateRequest](certificateupdaterequest.md)
  The request body you use to update a certificate activation status.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificateresponse)*