# Read and download certificate information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a certificate and download the certificate data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/certificates/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `name`, `identifier`, `certificates`
- `include` ([string]): **Allowed Values**: `passTypeId`

## Responses

- `200` OK (`CertificateResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting certificate infomation and data
- [List and download certificates](./get-v1-certificates.md)
  Find and list certificates and download their data.
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-certificates-_id_)*