# List passtypeid ids for a certificate

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all PassTypeIDId Ids for a specific certificate.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/certificates/{id}/relationships/passTypeId`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`CertificatePassTypeIdLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting certificate infomation and data
- [List and download certificates](./get-v1-certificates.md)
  Find and list certificates and download their data.
- [Read and download certificate information](./get-v1-certificates-_id_.md)
  Get information about a certificate and download the certificate data.
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-certificates-_id_-relationships-passtypeid)*