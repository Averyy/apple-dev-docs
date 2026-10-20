# Read and Download Certificate Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a certificate and download the certificate data.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/certificates/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `certificates`, `identifier`, `name`
- `include` ([string]): **Allowed Values**: `passTypeId`

## Responses

- `200` OK (`CertificateResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.

## See Also

### Getting Certificate Infomation and Data
- [List and Download Certificates](./list-and-download-certificates.md)
  Find and list certificates and download their data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-and-download-certificate-information)*