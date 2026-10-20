# Create a certificate

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a new certificate using a certificate signing request.

**Availability**:
- App Store Connect API 1.1+

## Mentions

- [Managing merchant IDs and Payment Processing certificates](./managing-payment-processing-certificates.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/certificates`

## Request Body

**Content-Type**: `application/json`  
**Type**: `CertificateCreateRequest`

## Responses

- `201` Created (`CertificateResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and modifying certificates
- [Modify a Certificate](./patch-v1-certificates-_id_.md)
  Update the activation status for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-certificates)*