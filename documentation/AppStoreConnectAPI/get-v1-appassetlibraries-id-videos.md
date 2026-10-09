# List related videos

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the video assets in an app’s asset library.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/videos?limit=1
```

**Response**:

```json
{
  "data" : [ {
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
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/videos"
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

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraries/{id}/videos`

## Parameters

- `filter[category]` ([string]): Filter the returned app asset library videos by category.
- `filter[state]` ([string]): Filter the returned app asset library videos by state.
- `filter[referenceName]` ([string]): Filter the returned app asset library videos by reference name.
- `filter[specId]` ([string]): Filter the returned app asset library videos by specification ID.
- `filter[id]` ([string]): Filter the returned app asset library videos by resource ID.
- `sort` ([string]): Attributes by which to sort.
- `fields[appAssetLibraryVideos]` ([string]): Additional fields to include for each app asset library video resource returned by the response.
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `limit` (integer): The maximum number of app asset library video resources to return.
- `include` ([string]): The relationship data to include in the response.
- `limit[placements]` (integer): The maximum number of related placement resources to return.

## See Also

- [List related images](get-v1-appassetlibraries-_id_-images.md)
  List the image assets in an app’s asset library.
- [List the image IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-images.md)
  Get a list of image asset resource IDs for a specific asset library.
- [List the video IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-videos.md)
  Get a list of video asset resource IDs for a specific asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraries-_id_-videos)*