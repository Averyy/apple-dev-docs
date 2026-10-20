# Create an app event screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library image`](./post-v1-appassetlibraryimages.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEventScreenshots`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEventScreenshotCreateRequest`

## Responses

- `201` Created (`AppEventScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List the Images for an In-App Event](./get-v1-appeventscreenshots-_id_.md)
- [Update an app event screenshot](./patch-v1-appeventscreenshots-_id_.md)
- [Delete an app event screenshot](./delete-v1-appeventscreenshots-_id_.md)
  Delete a specific screenshot from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appeventscreenshots)*