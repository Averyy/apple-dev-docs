# Delete an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an app screenshot set and all of its screenshots.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Delete an app asset library placement`](./delete-v1-appassetlibraryplacements-_id_.md) instead.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot set resource ID from the [`List all app screenshot sets for an app store version localization`](./get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Deleting Screenshot Sets
- [Create an app screenshot set](./post-v1-appscreenshotsets.md)
  Add a new screenshot set to an App Store version localization for a specific screenshot type and display size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appscreenshotsets-_id_)*