# List All App Store Version Localizations for an App Store Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localized, version-level information about an app, for all locales.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appStoreVersionLocalizations`

## Parameters

- `filter[locale]` ([string])
- `fields[appScreenshotSets]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[appPreviewSets]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])
- `limit` (integer)
- `limit[appScreenshotSets]` (integer)
- `limit[appPreviewSets]` (integer)
- `include` ([string])
- `fields[appKeywords]` ([string])
- `limit[searchKeywords]` (integer)

## See Also

- [Read App Store Version Localization Information](get-v1-appstoreversionlocalizations-_id_.md)
  Read localized version-level information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appstoreversionlocalizations)*