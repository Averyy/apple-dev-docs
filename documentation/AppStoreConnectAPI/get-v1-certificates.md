# List and download certificates

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list certificates and download their data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/certificates`

## Parameters

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `filter[id]` ([string])
- `filter[serialNumber]` ([string])
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `displayName`, `-displayName`, `certificateType`, `-certificateType`, `serialNumber`, `-serialNumber`, `id`, `-id`
- `filter[certificateType]` ([string]): **Allowed Values**: `APPLE_PAY`, `APPLE_PAY_MERCHANT_IDENTITY`, `APPLE_PAY_PSP_IDENTITY`, `APPLE_PAY_RSA`, `DEVELOPER_ID_KEXT`, `DEVELOPER_ID_KEXT_G2`, `DEVELOPER_ID_APPLICATION`, `DEVELOPER_ID_APPLICATION_G2`, `DEVELOPMENT`, `DISTRIBUTION`, `IDENTITY_ACCESS`, `IOS_DEVELOPMENT`, `IOS_DISTRIBUTION`, `MAC_APP_DISTRIBUTION`, `MAC_INSTALLER_DISTRIBUTION`, `MAC_APP_DEVELOPMENT`, `PASS_TYPE_ID`, `PASS_TYPE_ID_WITH_NFC`
- `filter[displayName]` ([string])
- `fields[passTypeIds]` ([string]): **Allowed Values**: `name`, `identifier`, `certificates`
- `include` ([string]): **Allowed Values**: `passTypeId`

## Responses

- `200` OK (`CertificatesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting certificate infomation and data
- [Read and download certificate information](./get-v1-certificates-_id_.md)
  Get information about a certificate and download the certificate data.
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-certificates)*