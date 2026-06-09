# Certificate

**Framework**: App Store Connect API  
**Kind**: dictionary

A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object Certificate
```

## Topics

### Objects
- [object Certificate.Attributes](certificate/attributes-data.dictionary.md)
  Attributes that describe a Certificates resource.
### Dictionaries
- [object Certificate.Relationships](certificate/relationships-data.dictionary.md)

## Properties

- `attributes` (Certificate.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (Certificate.Relationships)

## See Also

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
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificate)*