# List all app screenshot sets for an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all screenshot sets for a specific localization.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This relationship is deprecated. Use the [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) relationship instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/appScreenshotSets`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](./get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

### Query Parameters

- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.

  **Allowed Values**: `screenshotDisplayType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`
- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `appScreenshotSet`
- `filter[screenshotDisplayType]` ([string]): Filter the returned app screenshot sets by screenshot display type.

  **Allowed Values**: `APP_IPHONE_67`, `APP_IPHONE_61`, `APP_IPHONE_65`, `APP_IPHONE_58`, `APP_IPHONE_55`, `APP_IPHONE_47`, `APP_IPHONE_40`, `APP_IPHONE_35`, `APP_IPAD_PRO_3GEN_129`, `APP_IPAD_PRO_3GEN_11`, `APP_IPAD_PRO_129`, `APP_IPAD_105`, `APP_IPAD_97`, `APP_DESKTOP`, `APP_WATCH_ULTRA`, `APP_WATCH_SERIES_10`, `APP_WATCH_SERIES_7`, `APP_WATCH_SERIES_4`, `APP_WATCH_SERIES_3`, `APP_APPLE_TV`, `APP_APPLE_VISION_PRO`, `IMESSAGE_APP_IPHONE_67`, `IMESSAGE_APP_IPHONE_61`, `IMESSAGE_APP_IPHONE_65`, `IMESSAGE_APP_IPHONE_58`, `IMESSAGE_APP_IPHONE_55`, `IMESSAGE_APP_IPHONE_47`, `IMESSAGE_APP_IPHONE_40`, `IMESSAGE_APP_IPAD_PRO_3GEN_129`, `IMESSAGE_APP_IPAD_PRO_3GEN_11`, `IMESSAGE_APP_IPAD_PRO_129`, `IMESSAGE_APP_IPAD_105`, `IMESSAGE_APP_IPAD_97`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`
- `limit` (integer): The maximum number of app screenshot set resources to return.

  **Maximum**: `200`
- `limit[appScreenshots]` (integer): The maximum number of related app screenshot resources to return.

  **Maximum**: `50`
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app screenshot sets by App Store version experiment treatment localization.
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app screenshot sets by app custom product page localization.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.

  **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.

  **Allowed Values**: `locale`, `appStoreVersionExperimentTreatment`, `appScreenshotSets`, `appPreviewSets`, `placements`
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

  **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`

## Responses

- `200` OK (`AppScreenshotSetsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Information from a Localization
- [List all app preview sets for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md)
  List all app preview sets for a specific localization.
- [List preview set IDs for an App Store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-appscreenshotsets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-appscreenshotsets)*