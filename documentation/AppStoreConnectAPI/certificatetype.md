# CertificateType

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

Literal values that represent types of signing certificates.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```
string CertificateType
```

## Possible Values

- `APPLE_PAY`
- `APPLE_PAY_MERCHANT_IDENTITY`
- `APPLE_PAY_PSP_IDENTITY`
- `APPLE_PAY_RSA`
- `DEVELOPER_ID_KEXT`
- `DEVELOPER_ID_KEXT_G2`
- `DEVELOPER_ID_APPLICATION`
- `DEVELOPER_ID_APPLICATION_G2`
- `DEVELOPMENT`
- `DISTRIBUTION`
- `IDENTITY_ACCESS`
- `IOS_DEVELOPMENT`
- `IOS_DISTRIBUTION`
- `MAC_APP_DISTRIBUTION`
- `MAC_INSTALLER_DISTRIBUTION`
- `MAC_APP_DEVELOPMENT`
- `PASS_TYPE_ID`
- `PASS_TYPE_ID_WITH_NFC`

## Mentions

- [App Store Connect API 3.7 release notes](./app-store-connect-api-3-7-release-notes.md)

## See Also

### Object and data types
- [object Certificate](./certificate.md)
  A code signing certificate registered in your Apple developer account, used for development, distribution, or provisioning.
- [object CertificatesWithoutIncludesResponse](./certificateswithoutincludesresponse.md)
  A response containing a list of certificates, without related resources.
- [object CertificateCreateRequest](./certificatecreaterequest.md)
  The request body you use to create a Certificate.
- [object CertificateResponse](./certificateresponse.md)
  The response body for endpoints that create or read a single signing certificate.
- [object CertificatesResponse](./certificatesresponse.md)
  The response body for endpoints that list signing certificates.
- [object CertificateUpdateRequest](./certificateupdaterequest.md)
  The request body you use to update a certificate activation status.
- [object CertificatePassTypeIdLinkageResponse](./certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/certificatetype)*