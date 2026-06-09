# CertificateUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a certificate activation status.

**Availability**:
- App Store Connect API 3.8+

## Declaration

```swift
object CertificateUpdateRequest
```

## Topics

### Dictionaries
- [object CertificateUpdateRequest.Data](certificateupdaterequest/data-data.dictionary.md)
  The data structure that represent a certificate update request resource.

## Properties

- `data` (CertificateUpdateRequest.Data) *(required)*

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
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificateupdaterequest)*