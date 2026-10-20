# Create an app event video clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve a video clip asset for an in-app event.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library video`](./post-v1-appassetlibraryvideos.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEventVideoClips`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEventVideoClipCreateRequest`

## Responses

- `201` Created (`AppEventVideoClipResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read app event video clip information](./get-v1-appeventvideoclips-_id_.md)
  Get information about a specific video clip for an in-app event.
- [Modify an app event video clip](./patch-v1-appeventvideoclips-_id_.md)
  Commit an uploaded video clip asset for an in-app event.
- [Delete an app event video clip](./delete-v1-appeventvideoclips-_id_.md)
  Delete a specific video clip from an in-app event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appeventvideoclips)*