# List all app preview sets for an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all app preview sets for a specific localization.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/appPreviewSets`

## Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.
- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.
- `filter[previewType]` ([string]): Filter the returned app preview sets by preview type.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app preview set resources to return.
- `limit[appPreviews]` (integer): The maximum number of related app preview resources to return.
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app preview sets by app custom product page localization.
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app preview sets by App Store version experiment treatment localization.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

## See Also

- [List all app screenshot sets for an app store version localization](get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md)
  List all screenshot sets for a specific localization.
- [List preview set IDs for an App Store version localization](get-v1-appstoreversionlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version localization](get-v1-appstoreversionlocalizations-_id_-relationships-appscreenshotsets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-apppreviewsets)*