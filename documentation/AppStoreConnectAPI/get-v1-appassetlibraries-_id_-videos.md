# List related videos

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the video assets in an app’s asset library.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](./app-store-connect-api-4-5-1-release-notes.md)
- [Uploading and managing video assets](./uploading-and-managing-video-assets.md)

## Discussion

### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `filter[category]` ([string]): Filter the returned app asset library videos by category.

  **Allowed Values**: `CREATIVE_ASSETS`, `APP_SCREENSHOTS_AND_PREVIEWS`
- `filter[state]` ([string]): Filter the returned app asset library videos by state.

  **Allowed Values**: `AWAITING_UPLOAD`, `UPLOAD_COMPLETE`, `FAILED`, `COMPLETE`, `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `APPROVED`, `REJECTED`, `ARCHIVED`
- `filter[referenceName]` ([string]): Filter the returned app asset library videos by reference name.
- `filter[specId]` ([string]): Filter the returned app asset library videos by specification ID.
- `filter[id]` ([string]): Filter the returned app asset library videos by resource ID.
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `createdDate`, `-createdDate`, `lastModifiedDate`, `-lastModifiedDate`, `referenceName`, `-referenceName`
- `fields[appAssetLibraryVideos]` ([string]): Additional fields to include for each app asset library video resource returned by the response.

  **Allowed Values**: `category`, `createdDate`, `lastModifiedDate`, `fileName`, `fileSize`, `previewFrameImage`, `previewFrameTimeCode`, `referenceName`, `specId`, `state`, `stateDetails`, `uploadOperations`, `videoAsset`, `placements`
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.

  **Allowed Values**: `mediaType`, `placementType`, `placementGroup`, `createdDate`, `lastModifiedDate`, `state`, `stateDetails`, `image`, `video`, `appEventLocalization`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`
- `limit` (integer): The maximum number of app asset library video resources to return.

  **Maximum**: `200`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `placements`
- `limit[placements]` (integer): The maximum number of related placement resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`AppAssetLibraryVideosResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting assets in a library
- [List related images](./get-v1-appassetlibraries-_id_-images.md)
  List the image assets in an app’s asset library.
- [List the image IDs for an app asset library](./get-v1-appassetlibraries-_id_-relationships-images.md)
  Get a list of image asset resource IDs for a specific asset library.
- [List the video IDs for an app asset library](./get-v1-appassetlibraries-_id_-relationships-videos.md)
  Get a list of video asset resource IDs for a specific asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraries-_id_-videos)*