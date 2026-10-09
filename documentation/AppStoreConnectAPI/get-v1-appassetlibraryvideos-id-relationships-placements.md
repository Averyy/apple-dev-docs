# List the placement IDs for an app asset library video

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of placement resource IDs for a specific app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/relationships/placements?limit=1
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryPlacements",
    "id" : "2e000005-e036-8f0b-8f25-6dbc2baa784a"
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/relationships/placements",
    "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/placements"
  },
  "meta" : {
    "paging" : {
      "total" : 1,
      "limit" : 1
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/{id}/relationships/placements`

## Parameters

- `limit` (integer): The maximum number of app asset library placement resource identifiers to return.

## See Also

- [Read an app asset library video](get-v1-appassetlibraryvideos-_id_.md)
  Get information about an app asset library video.
- [List related placements](get-v1-appassetlibraryvideos-_id_-placements.md)
  List the placements that reuse an app asset library video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryvideos-_id_-relationships-placements)*