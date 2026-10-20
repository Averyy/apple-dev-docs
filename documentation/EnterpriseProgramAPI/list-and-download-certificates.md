# List and Download Certificates

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list certificates and download their data.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/certificates`

## Parameters

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `certificates`, `identifier`, `name`
- `filter[certificateType]` ([string]): **Allowed Values**: `IOS_DEVELOPMENT`, `IOS_DISTRIBUTION`, `MAC_APP_DISTRIBUTION`, `MAC_INSTALLER_DISTRIBUTION`, `MAC_APP_DEVELOPMENT`, `DEVELOPER_ID_KEXT`, `DEVELOPER_ID_APPLICATION`, `DEVELOPMENT`, `DISTRIBUTION`, `PASS_TYPE_ID`, `PASS_TYPE_ID_WITH_NFC`
- `filter[displayName]` ([string])
- `filter[id]` ([string])
- `filter[serialNumber]` ([string])
- `include` ([string]): **Allowed Values**: `passTypeId`
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `certificateType`, `-certificateType`, `displayName`, `-displayName`, `id`, `-id`, `serialNumber`, `-serialNumber`

## Responses

- `200` OK (`CertificatesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.

## See Also

### Getting Certificate Infomation and Data
- [Read and Download Certificate Information](./read-and-download-certificate-information.md)
  Get information about a certificate and download the certificate data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-and-download-certificates)*