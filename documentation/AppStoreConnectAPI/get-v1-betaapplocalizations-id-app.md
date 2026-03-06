# Read the App Information of a Beta App Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the app information associated with a specific beta app localization.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/{id}/app`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.

## See Also

- [List Beta App Localizations](get-v1-betaapplocalizations.md)
  Find and list beta app localizations for all apps and locales.
- [Read Beta App Localization Information](get-v1-betaapplocalizations-_id_.md)
  Get localized beta app information for a specific app and locale.
- [GET /v1/betaAppLocalizations/{id}/relationships/app](get-v1-betaapplocalizations-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaapplocalizations-_id_-app)*