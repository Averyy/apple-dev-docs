# List all app store version localizations for an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localized, version-level information about an app, for all locales.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appStoreVersionLocalizations`

## Parameters

- `filter[locale]` ([string]): Filter the returned App Store version localizations by locale.
- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.
- `limit` (integer): The maximum number of App Store version localization resources to return.
- `limit[appScreenshotSets]` (integer): The maximum number of related app screenshot set resources to return.
- `limit[appPreviewSets]` (integer): The maximum number of related app preview set resources to return.
- `include` ([string]): The relationship data to include in the response.
- `fields[appKeywords]` ([string])
- `limit[searchKeywords]` (integer)

## See Also

- [Read app store version localization information](get-v1-appstoreversionlocalizations-_id_.md)
  Read localized version-level information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appstoreversionlocalizations)*