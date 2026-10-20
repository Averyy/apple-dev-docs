# Create an app preview set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new app preview set to an App Store version localization for a specific app preview type and display size.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library placement`](./post-v1-appassetlibraryplacements.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appPreviewSets`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppPreviewSetCreateRequest`

## Responses

- `201` Created (`AppPreviewSetResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Deleting Preview Sets
- [Delete an app preview set](./delete-v1-apppreviewsets-_id_.md)
  Delete an app preview set and all of its previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-apppreviewsets)*