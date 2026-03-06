# List Beta App Localizations

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta app localizations for all apps and locales.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppLocalizations`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaAppLocalizations]` ([string]): Fields to return for included related types.
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[locale]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.

## See Also

- [Read Beta App Localization Information](get-v1-betaapplocalizations-_id_.md)
  Get localized beta app information for a specific app and locale.
- [Read the App Information of a Beta App Localization](get-v1-betaapplocalizations-_id_-app.md)
  Get the app information associated with a specific beta app localization.
- [GET /v1/betaAppLocalizations/{id}/relationships/app](get-v1-betaapplocalizations-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaapplocalizations)*