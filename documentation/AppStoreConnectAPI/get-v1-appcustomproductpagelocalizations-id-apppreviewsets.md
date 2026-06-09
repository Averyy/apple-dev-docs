# List App Preview Sets for a Custom Product Page Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the app preview sets for a specific custom product page localization.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}/appPreviewSets`

## Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.
- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app preview sets by App Store version experiment treatment localization.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app preview sets by App Store version localization.
- `filter[previewType]` ([string]): Filter the returned app preview sets by preview type.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app preview set resources to return.
- `limit[appPreviews]` (integer): The maximum number of related app previews resources to return.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

## See Also

- [Create an app preview set](post-v1-apppreviewsets.md)
  Add a new app preview set to an App Store version localization for a specific app preview type and display size.
- [Delete an app preview set](delete-v1-apppreviewsets-_id_.md)
  Delete an app preview set and all of its previews.
- [List all app previews for an app preview set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get all app preview ids for an app preview set](get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.
- [Replace all app previews for an app preview set](patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.
- [Create an app preview set](post-v1-apppreviewsets.md)
  Add a new app preview set to an App Store version localization for a specific app preview type and display size.
- [Delete an app preview set](delete-v1-apppreviewsets-_id_.md)
  Delete an app preview set and all of its previews.
- [List all app previews for an app preview set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get all app preview ids for an app preview set](get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.
- [Replace all app previews for an app preview set](patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpagelocalizations-_id_-apppreviewsets)*