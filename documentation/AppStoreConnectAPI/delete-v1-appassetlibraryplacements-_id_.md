# Delete an app asset library placement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an app asset library placement.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Placing assets on your App Store surfaces](./placing-assets-on-your-app-store-surfaces.md)

#### Discussion

##### Example Request and Response

**Request**:

```
DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/2e000005-e036-8f0b-8f25-6dbc2baa784a
```

**Response**:

```
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing placements
- [Create an app asset library placement](./post-v1-appassetlibraryplacements.md)
  Create an app asset library placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appassetlibraryplacements-_id_)*