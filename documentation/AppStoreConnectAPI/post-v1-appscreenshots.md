# Create an app screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new screenshot to a screenshot set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library image`](./post-v1-appassetlibraryimages.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appScreenshots`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppScreenshotCreateRequest`

## Responses

- `201` Created (`AppScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Screenshots
- [Modify an app screenshot](./patch-v1-appscreenshots-_id_.md)
  Commit an app screenshot after uploading it.
- [Delete an app screenshot](./delete-v1-appscreenshots-_id_.md)
  Delete an app screenshot that is associated with a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appscreenshots)*