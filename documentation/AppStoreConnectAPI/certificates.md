# Certificates

**Framework**: App Store Connect API

Create, download, and revoke signing certificates for app development and distribution.

#### Overview

The `certificates` resource represents the digital certificates you use to sign your iOS or Mac apps for development and distribution. You can create new certificates, revoke existing certificates, and download certificates.

> **Note**:  You can only create Developer ID certificates for macOS through the Apple Developer website or Xcode. For more information, see [`Security`](https://developer.apple.comhttps://developer.apple.com/developer-id/).

## Topics

### Creating and modifying certificates
- [Create a Certificate](post-v1-certificates.md)
  Create a new certificate using a certificate signing request.
- [Modify a certificate](patch-v1-certificates-_id_.md)
  Update the activation status for a specific certificate.
### Getting certificate infomation and data
- [List and Download Certificates](get-v1-certificates.md)
  Find and list certificates and download their data.
- [Read and Download Certificate Information](get-v1-certificates-_id_.md)
  Get information about a certificate and download the certificate data.
- [List PassTypeID Ids for a certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [GET /v1/certificates/{id}/relationships/passTypeId](get-v1-certificates-_id_-relationships-passtypeid.md)
### Revoking certificates
- [Revoke a Certificate](delete-v1-certificates-_id_.md)
  Revoke a lost, stolen, compromised, or expiring signing certificate.
### Object and data types
- [object Certificate](certificate.md)
  The data structure that represents a Certificates resource.
- [object CertificatesWithoutIncludesResponse](certificateswithoutincludesresponse.md)
- [object CertificateCreateRequest](certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificateResponse](certificateresponse.md)
  A response that contains a single Certificates resource.
- [object CertificatesResponse](certificatesresponse.md)
  A response that contains a list of Certificates resources.
- [object CertificateUpdateRequest](certificateupdaterequest.md)
  The request body you use to update a certificate activation status.
- [type CertificateType](certificatetype.md)
  Literal values that represent types of signing certificates.
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Devices](devices.md)
  Register devices for development and testing.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles that enable app installations for development and distribution.
- [Merchant ID](merchantids.md)
  Manage your merchant ID for Apple Pay.
- [Pass type Ids](pass-type-id.md)
  Create, download, and revoke pass type ids for app development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificates)*