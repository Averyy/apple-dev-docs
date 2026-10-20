# List all app screenshots for an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all ordered screenshots in a screenshot set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library placement`](./get-v1-appassetlibraryplacements-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}/appScreenshots`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot set resource ID from the [`List all app screenshot sets for an app store version localization`](./get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md) response.

### Query Parameters

- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `appScreenshotSet`
- `limit` (integer): The maximum number of app screenshot resources to return.

  **Maximum**: `200`
- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.

  **Allowed Values**: `screenshotDisplayType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appScreenshotSet`

## Responses

- `200` OK (`AppScreenshotsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing and Reordering All Screenshots in a Set
- [Get all app screenshot ids for an app screenshot set](./get-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Get the ordered screenshot IDs in a screenshot set.
- [Replace all app screenshots for an app screenshot set](./patch-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Change the order of the screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshotsets-_id_-appscreenshots)*