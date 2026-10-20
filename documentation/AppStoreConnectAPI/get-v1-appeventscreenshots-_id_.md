# List the Images for an In-App Event

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library image`](./get-v1-appassetlibraryimages-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event screenshot resource ID from the [`List all screenshots for an app event localization`](./get-v1-appeventlocalizations-_id_-appeventscreenshots.md) response.

### Query Parameters

- `fields[appEventScreenshots]` ([string]): Additional fields to include for each app event screenshot resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `assetToken`, `uploadOperations`, `assetDeliveryState`, `appEventAssetType`, `appEventLocalization`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appEventLocalization`
- `fields[appEventLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `shortDescription`, `longDescription`, `appEvent`, `appEventScreenshots`, `appEventVideoClips`, `placements`

## Responses

- `200` OK (`AppEventScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Update an app event screenshot](./patch-v1-appeventscreenshots-_id_.md)
- [Create an app event screenshot](./post-v1-appeventscreenshots.md)
- [Delete an app event screenshot](./delete-v1-appeventscreenshots-_id_.md)
  Delete a specific screenshot from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventscreenshots-_id_)*