# Read an app asset library video

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502
```

**Response**:

```json
{
  "data" : {
    "type" : "appAssetLibraryVideos",
    "id" : "3b100005-e036-8f0b-8021-77aa41c6b502",
    "attributes" : {
      "category" : "APP_SCREENSHOTS_AND_PREVIEWS",
      "createdDate" : "2026-08-11T22:51:04Z",
      "lastModifiedDate" : "2026-08-11T22:53:22Z",
      "fileName" : "app-preview-6-9.mp4",
      "fileSize" : 31457280,
      "previewFrameImage" : {
        "image" : {
          "templateUrl" : "https://is1.mzstatic.com/image/thumb/AOsFKpK1JfF_vrxSCSbIew/{w}x{h}bb.{f}",
          "width" : 886,
          "height" : 1920
        },
        "state" : "COMPLETE"
      },
      "previewFrameTimeCode" : "00:00:03:00",
      "referenceName" : "Fall campaign preview",
      "specId" : "1861fdcb-eb99-59e6-8c6c-5a07479d9a84",
      "state" : "PREPARE_FOR_SUBMISSION",
      "stateDetails" : null,
      "videoAsset" : "https://video-ssl.itunes.apple.com/itunes-assets/Video/v4/preview.m3u8"
    },
    "relationships" : {
      "placements" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/relationships/placements",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/placements"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/{id}`

## Parameters

- `fields[appAssetLibraryVideos]` ([string]): Additional fields to include for each app asset library video resource returned by the response.
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[placements]` (integer): The maximum number of related placement resources to return.

## See Also

- [List related placements](get-v1-appassetlibraryvideos-_id_-placements.md)
  List the placements that reuse an app asset library video.
- [List the placement IDs for an app asset library video](get-v1-appassetlibraryvideos-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific app asset library video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryvideos-_id_)*