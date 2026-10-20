# Delete an app event screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a specific screenshot from an in-app event.

**Availability**:
- App Store Connect API 1.7+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Delete an app asset library image`](./delete-v1-appassetlibraryimages-_id_.md) instead.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appEventScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app event screenshot resource ID from the [`List all screenshots for an app event localization`](./get-v1-appeventlocalizations-_id_-appeventscreenshots.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List the Images for an In-App Event](./get-v1-appeventscreenshots-_id_.md)
- [Update an app event screenshot](./patch-v1-appeventscreenshots-_id_.md)
- [Create an app event screenshot](./post-v1-appeventscreenshots.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appeventscreenshots-_id_)*