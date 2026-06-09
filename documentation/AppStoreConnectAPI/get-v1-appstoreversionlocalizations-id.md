# Read app store version localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read localized version-level information.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}`

## Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.
- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appPreviewSets]` (integer): The maximum number of related app preview set resources to return.
- `limit[appScreenshotSets]` (integer): The maximum number of related app screenshot set resources to return.
- `fields[appStoreVersions]` ([string])
- `limit[searchKeywords]` (integer)

## See Also

- [List all app store version localizations for an app store version](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md)
  Get a list of localized, version-level information about an app, for all locales.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_)*