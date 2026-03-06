# CertificateResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary

A response that contains a single Certificates resource.

## Declaration

```swift
object CertificateResponse
```

## Topics

### Related Documentation
- [Create a Certificate](create-a-certificate.md)
  Create a new certificate using a certificate signing request.

## Properties

- `data` (Certificate) *(required)*: The resource data.
- `included` ([PassTypeId])
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object Certificate](certificate.md)
  The data structure that represents a Certificates resource.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
  A response that contains a single certificate resource without includes.
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificatesResponse](certificatesresponse.md)
  A response that contains a list of Certificates resources.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/certificateresponse)*