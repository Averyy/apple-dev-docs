# Certificate

**Framework**: Enterprise Program API  
**Kind**: dictionary

The data structure that represents a Certificates resource.

## Declaration

```swift
object Certificate
```

## Topics

### Objects
- [object Certificate.Attributes](certificate/attributes-data.dictionary.md)
  Attributes that describe a Certificates resource.
- [object Certificate.Relationships](certificate/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `attributes` (Certificate.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (Certificate.Relationships)

## See Also

- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response that contains a single certificate resource without includes.
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificateResponse](certificateresponse.md)
  A response that contains a single Certificates resource.
- [object CertificatesResponse](certificatesresponse.md)
  A response that contains a list of Certificates resources.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/certificate)*