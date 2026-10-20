# Read app screenshot information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about an app screenshot and its upload and processing status.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library image`](./get-v1-appassetlibraryimages-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot resource ID from the [`List all app screenshots for an app screenshot set`](./get-v1-appscreenshotsets-_id_-appscreenshots.md) response.

### Query Parameters

- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `assetToken`, `assetType`, `uploadOperations`, `assetDeliveryState`, `appScreenshotSet`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appScreenshotSet`
- `fields[appScreenshotSets]` ([string]): **Allowed Values**: `screenshotDisplayType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`

## Responses

- `200` OK (`AppScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Screenshots and Reading Information
- [List all app screenshots for an app screenshot set](./get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshots-_id_)*