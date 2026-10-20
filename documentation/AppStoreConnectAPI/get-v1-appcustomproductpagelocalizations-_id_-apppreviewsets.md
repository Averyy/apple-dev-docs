# List App Preview Sets for a Custom Product Page Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the app preview sets for a specific custom product page localization.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This relationship is deprecated. Use the [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) relationship instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}/appPreviewSets`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page localization resource ID from the [`List Custom Product Pages Localizations`](./get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md) response.

### Query Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.

  **Allowed Values**: `previewType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `previewFrameTimeCode`, `mimeType`, `videoUrl`, `previewFrameImage`, `previewImage`, `uploadOperations`, `assetDeliveryState`, `videoDeliveryState`, `appPreviewSet`
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app preview sets by App Store version experiment treatment localization.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app preview sets by App Store version localization.
- `filter[previewType]` ([string]): Filter the returned app preview sets by preview type.

  **Allowed Values**: `IPHONE_67`, `IPHONE_61`, `IPHONE_65`, `IPHONE_58`, `IPHONE_55`, `IPHONE_47`, `IPHONE_40`, `IPHONE_35`, `IPAD_PRO_3GEN_129`, `IPAD_PRO_3GEN_11`, `IPAD_PRO_129`, `IPAD_105`, `IPAD_97`, `DESKTOP`, `APPLE_TV`, `APPLE_VISION_PRO`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `limit` (integer): The maximum number of app preview set resources to return.

  **Maximum**: `200`
- `limit[appPreviews]` (integer): The maximum number of related app previews resources to return.

  **Maximum**: `50`
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.

  **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.

  **Allowed Values**: `locale`, `appStoreVersionExperimentTreatment`, `appScreenshotSets`, `appPreviewSets`, `placements`
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

  **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`

## Responses

- `200` OK (`AppPreviewSetsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Related Documentation
- [Create an app preview set](./post-v1-apppreviewsets.md)
  Add a new app preview set to an App Store version localization for a specific app preview type and display size.
- [Delete an app preview set](./delete-v1-apppreviewsets-_id_.md)
  Delete an app preview set and all of its previews.
- [List all app previews for an app preview set](./get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get all app preview ids for an app preview set](./get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.
- [Replace all app previews for an app preview set](./patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.
### Endpoints
- [Create an app preview set](./post-v1-apppreviewsets.md)
  Add a new app preview set to an App Store version localization for a specific app preview type and display size.
- [Delete an app preview set](./delete-v1-apppreviewsets-_id_.md)
  Delete an app preview set and all of its previews.
- [List all app previews for an app preview set](./get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get all app preview ids for an app preview set](./get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.
- [Replace all app previews for an app preview set](./patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpagelocalizations-_id_-apppreviewsets)*