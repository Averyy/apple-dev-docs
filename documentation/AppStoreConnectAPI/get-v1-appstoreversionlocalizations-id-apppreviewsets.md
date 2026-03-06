# List All App Preview Sets for an App Store Version Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all app preview sets for a specific localization.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/appPreviewSets`

## Parameters

- `fields[appPreviewSets]` ([string])
- `fields[appPreviews]` ([string])
- `filter[previewType]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[appPreviews]` (integer)
- `filter[appCustomProductPageLocalization]` ([string])
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string])
- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])

## See Also

- [List All App Screenshot Sets for an App Store Version Localization](get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md)
  List all screenshot sets for a specific localization.
- [GET /v1/appStoreVersionLocalizations/{id}/relationships/appPreviewSets](get-v1-appstoreversionlocalizations-_id_-relationships-apppreviewsets.md)
- [GET /v1/appStoreVersionLocalizations/{id}/relationships/appScreenshotSets](get-v1-appstoreversionlocalizations-_id_-relationships-appscreenshotsets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-apppreviewsets)*