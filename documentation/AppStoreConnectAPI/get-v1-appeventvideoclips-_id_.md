# Read app event video clip information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific video clip for an in-app event.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library video`](./get-v1-appassetlibraryvideos-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventVideoClips/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event video clip resource ID from the [`List all video clips for an app event localization`](./get-v1-appeventlocalizations-_id_-appeventvideoclips.md) response.

### Query Parameters

- `fields[appEventVideoClips]` ([string]): Additional fields to include for each app event video clip resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `previewFrameTimeCode`, `videoUrl`, `previewFrameImage`, `previewImage`, `uploadOperations`, `assetDeliveryState`, `videoDeliveryState`, `appEventAssetType`, `appEventLocalization`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appEventLocalization`
- `fields[appEventLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `shortDescription`, `longDescription`, `appEvent`, `appEventScreenshots`, `appEventVideoClips`, `placements`

## Responses

- `200` OK (`AppEventVideoClipResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Modify an app event video clip](./patch-v1-appeventvideoclips-_id_.md)
  Commit an uploaded video clip asset for an in-app event.
- [Create an app event video clip](./post-v1-appeventvideoclips.md)
  Reserve a video clip asset for an in-app event.
- [Delete an app event video clip](./delete-v1-appeventvideoclips-_id_.md)
  Delete a specific video clip from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventvideoclips-_id_)*