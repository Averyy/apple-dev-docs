# Read Beta App Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get localized beta app information for a specific app and locale.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/{id}`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaAppLocalizations]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

## See Also

- [List Beta App Localizations](get-v1-betaapplocalizations.md)
  Find and list beta app localizations for all apps and locales.
- [Read the App Information of a Beta App Localization](get-v1-betaapplocalizations-_id_-app.md)
  Get the app information associated with a specific beta app localization.
- [GET /v1/betaAppLocalizations/{id}/relationships/app](get-v1-betaapplocalizations-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaapplocalizations-_id_)*