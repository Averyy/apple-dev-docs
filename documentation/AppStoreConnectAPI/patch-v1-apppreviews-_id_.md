# Modify an app preview

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit the app preview after uploading it, and update the poster frame timecode.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Modify an app asset library video`](./patch-v1-appassetlibraryvideos-_id_.md) instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appPreviews/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview resource ID from the [`List all app previews for an app preview set`](./get-v1-apppreviewsets-_id_-apppreviews.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppPreviewUpdateRequest`

## Responses

- `200` OK (`AppPreviewResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting App Previews
- [Create an app preview](./post-v1-apppreviews.md)
  Add a new app preview to a preview set.
- [Delete an app preview](./delete-v1-apppreviews-_id_.md)
  Delete an app preview within a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-apppreviews-_id_)*