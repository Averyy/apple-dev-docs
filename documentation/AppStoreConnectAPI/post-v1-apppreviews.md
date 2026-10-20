# Create an app preview

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new app preview to a preview set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library video`](./post-v1-appassetlibraryvideos.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appPreviews`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppPreviewCreateRequest`

## Responses

- `201` Created (`AppPreviewResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting App Previews
- [Modify an app preview](./patch-v1-apppreviews-_id_.md)
  Commit the app preview after uploading it, and update the poster frame timecode.
- [Delete an app preview](./delete-v1-apppreviews-_id_.md)
  Delete an app preview within a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-apppreviews)*