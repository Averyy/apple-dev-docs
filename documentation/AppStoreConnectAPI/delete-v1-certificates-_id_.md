# Revoke a certificate

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Revoke a lost, stolen, compromised, or expiring signing certificate.

**Availability**:
- App Store Connect API 1.1+

## Mentions

- [Managing merchant IDs and Payment Processing certificates](./managing-payment-processing-certificates.md)

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/certificates/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-certificates-_id_)*