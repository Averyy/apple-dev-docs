# List the video IDs for an app asset library

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of video asset resource IDs for a specific asset library.

**Availability**:
- App Store Connect API 4.5+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/videos?limit=1
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryVideos",
    "id" : "3b100005-e036-8f0b-8021-77aa41c6b502"
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/videos",
    "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/videos"
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

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraries/{id}/relationships/videos`

## Parameters

- `limit` (integer): The maximum number of app asset library video resource identifiers to return.

## See Also

- [List related images](get-v1-appassetlibraries-_id_-images.md)
  List the image assets in an app’s asset library.
- [List related videos](get-v1-appassetlibraries-_id_-videos.md)
  List the video assets in an app’s asset library.
- [List the image IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-images.md)
  Get a list of image asset resource IDs for a specific asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraries-_id_-relationships-videos)*