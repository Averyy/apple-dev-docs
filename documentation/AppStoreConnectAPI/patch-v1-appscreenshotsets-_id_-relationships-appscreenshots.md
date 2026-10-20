# Replace all app screenshots for an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Change the order of the screenshots in a screenshot set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library placement ordering request`](./post-v1-appassetlibraryplacementorderingrequests.md) instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}/relationships/appScreenshots`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot set resource ID from the [`List all app screenshot sets for an app store version localization`](./get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppScreenshotSetAppScreenshotsLinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing and Reordering All Screenshots in a Set
- [Get all app screenshot ids for an app screenshot set](./get-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Get the ordered screenshot IDs in a screenshot set.
- [List all app screenshots for an app screenshot set](./get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appscreenshotsets-_id_-relationships-appscreenshots)*