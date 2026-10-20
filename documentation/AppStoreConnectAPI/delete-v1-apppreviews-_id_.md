# Delete an app preview

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an app preview within a preview set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Delete an app asset library video`](./delete-v1-appassetlibraryvideos-_id_.md) instead.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appPreviews/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview resource ID from the [`List all app previews for an app preview set`](./get-v1-apppreviewsets-_id_-apppreviews.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting App Previews
- [Create an app preview](./post-v1-apppreviews.md)
  Add a new app preview to a preview set.
- [Modify an app preview](./patch-v1-apppreviews-_id_.md)
  Commit the app preview after uploading it, and update the poster frame timecode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-apppreviews-_id_)*