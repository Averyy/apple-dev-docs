# Replace all app previews for an app preview set

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Change the order of the app previews in a preview set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This endpoint is deprecated. Use [`Create an app asset library placement ordering request`](./post-v1-appassetlibraryplacementorderingrequests.md) instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}/relationships/appPreviews`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview set resource ID from the [`List all app preview sets for an app store version localization`](./get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppPreviewSetAppPreviewsLinkagesRequest`

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

### Listing and Reordering All Previews in a Set
- [List all app previews for an app preview set](./get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get all app preview ids for an app preview set](./get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-apppreviewsets-_id_-relationships-apppreviews)*