# Read app preview information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about an app preview and its upload and processing status.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library video`](./get-v1-appassetlibraryvideos-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviews/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview resource ID from the [`List all app previews for an app preview set`](./get-v1-apppreviewsets-_id_-apppreviews.md) response.

### Query Parameters

- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `previewFrameTimeCode`, `mimeType`, `videoUrl`, `previewFrameImage`, `previewImage`, `uploadOperations`, `assetDeliveryState`, `videoDeliveryState`, `appPreviewSet`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appPreviewSet`
- `fields[appPreviewSets]` ([string]): **Allowed Values**: `previewType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`

## Responses

- `200` OK (`AppPreviewResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing App Previews and Reading Information
- [List all app previews for an app preview set](./get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviews-_id_)*