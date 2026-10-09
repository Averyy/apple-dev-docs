# Delete an app asset library placement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app asset library placement.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/2e000005-e036-8f0b-8f25-6dbc2baa784a
```

**Response**:

```None
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create an app asset library placement](post-v1-appassetlibraryplacements.md)
  Create an app asset library placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appassetlibraryplacements-_id_)*