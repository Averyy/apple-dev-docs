# List all app previews for an app preview set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all ordered app previews in a preview set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library placement`](./get-v1-appassetlibraryplacements-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}/appPreviews`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview set resource ID from the [`List all app preview sets for an app store version localization`](./get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md) response.

### Query Parameters

- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `previewFrameTimeCode`, `mimeType`, `videoUrl`, `previewFrameImage`, `previewImage`, `uploadOperations`, `assetDeliveryState`, `videoDeliveryState`, `appPreviewSet`
- `limit` (integer): The maximum number of app preview resources to return.

  **Maximum**: `200`
- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.

  **Allowed Values**: `previewType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appPreviewSet`

## Responses

- `200` OK (`AppPreviewsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing and Reordering All Previews in a Set
- [Get all app preview ids for an app preview set](./get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.
- [Replace all app previews for an app preview set](./patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviewsets-_id_-apppreviews)*