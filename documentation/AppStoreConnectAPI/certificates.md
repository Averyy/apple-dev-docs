# Certificates

**Framework**: App Store Connect API

Create, download, and revoke signing certificates for app development and distribution.

#### Overview

The `certificates` resource represents the digital certificates you use to sign your iOS or Mac apps for development and distribution. You can create new certificates, revoke existing certificates, and download certificates.

> **Note**:  You can only create Developer ID certificates for macOS through the Apple Developer website or Xcode. For more information, see [`Security`](https://developer.apple.comhttps://developer.apple.com/developer-id/).

## Topics

### Creating and modifying certificates
- [Create a certificate](post-v1-certificates.md)
  Create a new certificate using a certificate signing request.
- [Modify a Certificate](patch-v1-certificates-_id_.md)
  Update the activation status for a specific certificate.
### Getting certificate infomation and data
- [List and download certificates](get-v1-certificates.md)
  Find and list certificates and download their data.
- [Read and download certificate information](get-v1-certificates-_id_.md)
  Get information about a certificate and download the certificate data.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.
### Revoking certificates
- [Revoke a certificate](delete-v1-certificates-_id_.md)
  Revoke a lost, stolen, compromised, or expiring signing certificate.
### Object and data types
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