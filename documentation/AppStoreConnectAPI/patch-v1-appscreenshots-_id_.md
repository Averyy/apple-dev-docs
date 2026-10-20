# Modify an app screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit an app screenshot after uploading it.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Modify an app asset library image`](./patch-v1-appassetlibraryimages-_id_.md) instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot resource ID from the [`List all app screenshots for an app screenshot set`](./get-v1-appscreenshotsets-_id_-appscreenshots.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppScreenshotUpdateRequest`

## Responses

- `200` OK (`AppScreenshotResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Screenshots
- [Create an app screenshot](./post-v1-appscreenshots.md)
  Add a new screenshot to a screenshot set.
- [Delete an app screenshot](./delete-v1-appscreenshots-_id_.md)
  Delete an app screenshot that is associated with a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appscreenshots-_id_)*