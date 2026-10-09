# Delete an app asset library image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing image assets](uploading-and-managing-image-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61
```

**Response**:

```None
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create an app asset library image](post-v1-appassetlibraryimages.md)
  Create an app asset library image.
- [Modify an app asset library image](patch-v1-appassetlibraryimages-_id_.md)
  Update an app asset library image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appassetlibraryimages-_id_)*