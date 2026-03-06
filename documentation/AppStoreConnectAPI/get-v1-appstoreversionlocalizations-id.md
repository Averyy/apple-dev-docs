# Read App Store Version Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read localized version-level information.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}`

## Parameters

- `fields[appPreviewSets]` ([string])
- `fields[appScreenshotSets]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])
- `include` ([string])
- `limit[appPreviewSets]` (integer)
- `limit[appScreenshotSets]` (integer)
- `limit[searchKeywords]` (integer)

## See Also

- [List All App Store Version Localizations for an App Store Version](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md)
  Get a list of localized, version-level information about an app, for all locales.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_)*