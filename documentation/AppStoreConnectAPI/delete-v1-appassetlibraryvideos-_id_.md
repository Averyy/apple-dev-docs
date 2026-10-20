# Delete an app asset library video

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502
```

**Response**:

```None
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create an app asset library video](post-v1-appassetlibraryvideos.md)
  Create an app asset library video.
- [Modify an app asset library video](patch-v1-appassetlibraryvideos-_id_.md)
  Update an app asset library video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appassetlibraryvideos-_id_)*