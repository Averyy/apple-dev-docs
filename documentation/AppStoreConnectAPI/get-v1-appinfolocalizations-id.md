# Read app info localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read localized app-level information.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfoLocalizations/{id}`

## Parameters

- `fields[appInfoLocalizations]` ([string]): Additional fields to include for each app info localization resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appInfos]` ([string])

## See Also

- [List all app info localizations for an app info](get-v1-appinfos-_id_-appinfolocalizations.md)
  Get a list of localized, app-level information for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfolocalizations-_id_)*