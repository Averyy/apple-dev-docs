# Modify an app asset library video

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502

{
  "data": {
    "type": "appAssetLibraryVideos",
    "id": "3b100005-e036-8f0b-8021-77aa41c6b502",
    "attributes": {
      "previewFrameTimeCode": "00:00:05:00"
    }
  }
}
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
        "state" : "PROCESSING"
      },
      "previewFrameTimeCode" : "00:00:05:00",
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

`PATCH https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

The request body you use to update an app asset library video.

## See Also

- [Create an app asset library video](post-v1-appassetlibraryvideos.md)
  Create an app asset library video.
- [Delete an app asset library video](delete-v1-appassetlibraryvideos-_id_.md)
  Delete an app asset library video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appassetlibraryvideos-_id_)*