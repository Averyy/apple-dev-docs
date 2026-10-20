# List all screenshot sets for an experiment treatment localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of screenshot sets for a specific App Store version experiment treatment localization.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This relationship is deprecated. Use the [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) relationship instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatmentLocalizations/{id}/appScreenshotSets`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version experiment treatment localization resource ID from the [`List all localizations for an app store version experiment treatment`](./get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md) response.

### Query Parameters

- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.

  **Allowed Values**: `screenshotDisplayType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`
- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `appScreenshotSet`
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app screenshot sets by app custom product page localization.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app screenshot sets by App Store version localization.
- `filter[screenshotDisplayType]` ([string]): Filter the returned app screenshot sets by screenshot display type.

  **Allowed Values**: `APP_IPHONE_67`, `APP_IPHONE_61`, `APP_IPHONE_65`, `APP_IPHONE_58`, `APP_IPHONE_55`, `APP_IPHONE_47`, `APP_IPHONE_40`, `APP_IPHONE_35`, `APP_IPAD_PRO_3GEN_129`, `APP_IPAD_PRO_3GEN_11`, `APP_IPAD_PRO_129`, `APP_IPAD_105`, `APP_IPAD_97`, `APP_DESKTOP`, `APP_WATCH_ULTRA`, `APP_WATCH_SERIES_10`, `APP_WATCH_SERIES_7`, `APP_WATCH_SERIES_4`, `APP_WATCH_SERIES_3`, `APP_APPLE_TV`, `APP_APPLE_VISION_PRO`, `IMESSAGE_APP_IPHONE_67`, `IMESSAGE_APP_IPHONE_61`, `IMESSAGE_APP_IPHONE_65`, `IMESSAGE_APP_IPHONE_58`, `IMESSAGE_APP_IPHONE_55`, `IMESSAGE_APP_IPHONE_47`, `IMESSAGE_APP_IPHONE_40`, `IMESSAGE_APP_IPAD_PRO_3GEN_129`, `IMESSAGE_APP_IPAD_PRO_3GEN_11`, `IMESSAGE_APP_IPAD_PRO_129`, `IMESSAGE_APP_IPAD_105`, `IMESSAGE_APP_IPAD_97`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`
- `limit` (integer): The maximum number of app screenshot set resources to return.

  **Maximum**: `200`
- `limit[appScreenshots]` (integer): The maximum number of related app screenshot resources to return.

  **Maximum**: `50`
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.

  **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.

  **Allowed Values**: `locale`, `appStoreVersionExperimentTreatment`, `appScreenshotSets`, `appPreviewSets`, `placements`
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

  **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`

## Responses

- `200` OK (`AppScreenshotSetsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read app store version experiment treatment localization information](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Get information about a specific App Store version experiment treatment localization.
- [List all preview sets for an experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-apppreviewsets.md)
  Get a list of preview sets for a specific App Store version experiment treatment localization.
- [List preview set IDs for an App Store version experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-appscreenshotsets.md)
- [Create an app store version experiment treatment localization](./post-v1-appstoreversionexperimenttreatmentlocalizations.md)
  Add a new localization for an App Store version experiment treatment.
- [Delete a treatment localization for an app store version experiment](./delete-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Delete localized metatdata that you configured for an App Store Version experiment treatment.
- [List related placements](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-placements.md)
  List the placements for an App Store version experiment treatment localization.
- [List the placement IDs for an App Store version experiment treatment localization](./get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific App Store version experiment treatment localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-appscreenshotsets)*