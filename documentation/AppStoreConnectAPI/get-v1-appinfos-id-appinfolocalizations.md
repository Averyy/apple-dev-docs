# List all app info localizations for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localized, app-level information for an app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/appInfoLocalizations`

## Parameters

- `fields[appInfoLocalizations]` ([string]): Fields to return for included related types.
- `fields[appInfos]` ([string]): Fields to return for included related types.
- `filter[locale]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of included related resources to return.

## See Also

- [Read app info localization information](get-v1-appinfolocalizations-_id_.md)
  Read localized app-level information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-appinfolocalizations)*