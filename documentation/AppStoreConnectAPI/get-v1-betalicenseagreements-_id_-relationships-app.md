# Get the app ID for a beta license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaLicenseAgreements/{id}/relationships/app`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`BetaLicenseAgreementAppLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Beta License Agreement Information
- [List beta license agreements](./get-v1-betalicenseagreements.md)
  Find and list beta license agreements for all apps.
- [Read beta license agreement information](./get-v1-betalicenseagreements-_id_.md)
  Get a specific beta license agreement.
- [Read the app information of a beta license agreement](./get-v1-betalicenseagreements-_id_-app.md)
  Get the app information for a specific beta license agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betalicenseagreements-_id_-relationships-app)*