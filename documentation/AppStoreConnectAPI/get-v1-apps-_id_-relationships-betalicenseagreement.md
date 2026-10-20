# Get the beta license agreement ID for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/betaLicenseAgreement`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppBetaLicenseAgreementLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting an app’s TestFlight details
- [Read the beta app review details resource of an app](./get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [Get the beta app review detail ID for an app](./get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Get the beta app review detail ID for an app](./get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the beta license agreement of an app](./get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [List all beta app localizations of an app](./get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
- [List beta app localization IDs for an app](./get-v1-apps-_id_-relationships-betaapplocalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-betalicenseagreement)*