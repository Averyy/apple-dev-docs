# Get the app ID for a beta app localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/{id}/relationships/app`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`BetaAppLocalizationAppLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Localization Information
- [List beta app localizations](./get-v1-betaapplocalizations.md)
  Find and list beta app localizations for all apps and locales.
- [Read beta app localization information](./get-v1-betaapplocalizations-_id_.md)
  Get localized beta app information for a specific app and locale.
- [Read the app information of a beta app localization](./get-v1-betaapplocalizations-_id_-app.md)
  Get the app information associated with a specific beta app localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaapplocalizations-_id_-relationships-app)*