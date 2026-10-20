# Delete an app screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an app screenshot that is associated with a screenshot set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Delete an app asset library image`](./delete-v1-appassetlibraryimages-_id_.md) instead.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appScreenshots/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot resource ID from the [`List all app screenshots for an app screenshot set`](./get-v1-appscreenshotsets-_id_-appscreenshots.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Screenshots
- [Create an app screenshot](./post-v1-appscreenshots.md)
  Add a new screenshot to a screenshot set.
- [Modify an app screenshot](./patch-v1-appscreenshots-_id_.md)
  Commit an app screenshot after uploading it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appscreenshots-_id_)*