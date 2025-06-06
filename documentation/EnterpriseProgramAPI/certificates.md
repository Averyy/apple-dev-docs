# Certificates

**Framework**: Enterpriseprogramapi

Create, download, and revoke signing certificates for app development and distribution.

#### Overview

The `certificates` resource represents the digital certificates you use to sign your apps for development and distribution. You can create new certificates, revoke existing certificates, and download certificates.

> **Note**:  You can only create Developer ID certificates for macOS through the Apple Developer website or Xcode. For more information, see [`Security`](https://developer.apple.comhttps://developer.apple.com/developer-id/).

## Topics

### Creating Certificates
- [Create a Certificate](create-a-certificate.md)
  Create a new certificate using a certificate signing request.
### Getting Certificate Infomation and Data
- [List and Download Certificates](list-and-download-certificates.md)
  Find and list certificates and download their data.
- [Read and Download Certificate Information](read-and-download-certificate-information.md)
  Get information about a certificate and download the certificate data.
### Revoking Certificates
- [Revoke a Certificate](revoke-a-certificate.md)
  Revoke a lost, stolen, compromised, or expiring signing certificate.
### Object and Data Types
- [object Certificate](certificate.md)
  The data structure that represents a Certificates resource.
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

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Devices](devices.md)
  Register devices for development and testing.
- [Pass Type Ids](passtypeids.md)
  Create, download, and revoke pass type ids for app development and distribution.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles for development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/EnterpriseProgramAPI/certificates)*