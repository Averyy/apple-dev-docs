# List all app preview sets for an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all app preview sets for a specific localization.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This relationship is deprecated. Use the [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) relationship instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/appPreviewSets`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](./get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

### Query Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.

  **Allowed Values**: `previewType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `previewFrameTimeCode`, `mimeType`, `videoUrl`, `previewFrameImage`, `previewImage`, `uploadOperations`, `assetDeliveryState`, `videoDeliveryState`, `appPreviewSet`
- `filter[previewType]` ([string]): Filter the returned app preview sets by preview type.

  **Allowed Values**: `IPHONE_67`, `IPHONE_61`, `IPHONE_65`, `IPHONE_58`, `IPHONE_55`, `IPHONE_47`, `IPHONE_40`, `IPHONE_35`, `IPAD_PRO_3GEN_129`, `IPAD_PRO_3GEN_11`, `IPAD_PRO_129`, `IPAD_105`, `IPAD_97`, `DESKTOP`, `APPLE_TV`, `APPLE_VISION_PRO`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `limit` (integer): The maximum number of app preview set resources to return.

  **Maximum**: `200`
- `limit[appPreviews]` (integer): The maximum number of related app preview resources to return.

  **Maximum**: `50`
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app preview sets by app custom product page localization.
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app preview sets by App Store version experiment treatment localization.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.

  **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.

  **Allowed Values**: `locale`, `appStoreVersionExperimentTreatment`, `appScreenshotSets`, `appPreviewSets`, `placements`
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

  **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`

## Responses

- `200` OK (`AppPreviewSetsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Information from a Localization
- [List all app screenshot sets for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md)
  List all screenshot sets for a specific localization.
- [List preview set IDs for an App Store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-appscreenshotsets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-apppreviewsets)*