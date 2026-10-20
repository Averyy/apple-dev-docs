# Read app preview set information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get an app preview set that includes its display target, language, and the previews it contains.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Read an app asset library placement`](./get-v1-appassetlibraryplacements-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview set resource ID from the [`List all app preview sets for an app store version localization`](./get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md) response.

### Query Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.

  **Allowed Values**: `previewType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `previewFrameTimeCode`, `mimeType`, `videoUrl`, `previewFrameImage`, `previewImage`, `uploadOperations`, `assetDeliveryState`, `videoDeliveryState`, `appPreviewSet`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `limit[appPreviews]` (integer): The maximum number of related app previews resources to return.

  **Maximum**: `50`
- `fields[appCustomProductPageLocalizations]` ([string]): **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): **Allowed Values**: `locale`, `appStoreVersionExperimentTreatment`, `appScreenshotSets`, `appPreviewSets`, `placements`
- `fields[appStoreVersionLocalizations]` ([string]): **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`

## Responses

- `200` OK (`AppPreviewSetResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviewsets-_id_)*