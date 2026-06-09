# CertificateCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create a Certificate.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object CertificateCreateRequest
```

## Topics

### Objects
- [object CertificateCreateRequest.Data](certificatecreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (CertificateCreateRequest.Data) *(required)*: The resource data.

## See Also

- [object Certificate](certificate.md)
  A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response containing a list of certificates, without related resources.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificatecreaterequest)*