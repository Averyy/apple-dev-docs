# List the image IDs for an app asset library

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of image asset resource IDs for a specific asset library.

**Availability**:
- App Store Connect API 4.5+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/images?limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryImages",
    "id" : "f4000005-e036-8f0b-8018-d259974bee61"
  }, {
    "type" : "appAssetLibraryImages",
    "id" : "c3000005-e036-8f0b-8038-36fbc8d1c4ae"
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/images",
    "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/images"
  },
  "meta" : {
    "paging" : {
      "total" : 2,
      "limit" : 2
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraries/{id}/relationships/images`

## Parameters

- `limit` (integer): The maximum number of app asset library image resource identifiers to return.

## See Also

- [List related images](get-v1-appassetlibraries-_id_-images.md)
  List the image assets in an app’s asset library.
- [List related videos](get-v1-appassetlibraries-_id_-videos.md)
  List the video assets in an app’s asset library.
- [List the video IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-videos.md)
  Get a list of video asset resource IDs for a specific asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraries-_id_-relationships-images)*