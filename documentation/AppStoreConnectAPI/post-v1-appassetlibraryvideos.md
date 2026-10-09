# Create an app asset library video

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos

{
  "data": {
    "type": "appAssetLibraryVideos",
    "attributes": {
      "fileName": "app-preview-6-9.mp4",
      "fileSize": 31457280,
      "category": "APP_SCREENSHOTS_AND_PREVIEWS",
      "previewFrameTimeCode": "00:00:03:00",
      "referenceName": "Fall campaign preview"
    },
    "relationships": {
      "assetLibrary": {
        "data": {
          "type": "appAssetLibraries",
          "id": "1234567890"
        }
      }
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
      "lastModifiedDate" : "2026-08-11T22:51:04Z",
      "fileName" : "app-preview-6-9.mp4",
      "fileSize" : 31457280,
      "previewFrameImage" : null,
      "previewFrameTimeCode" : "00:00:03:00",
      "referenceName" : "Fall campaign preview",
      "specId" : null,
      "state" : "AWAITING_UPLOAD",
      "stateDetails" : null,
      "videoAsset" : null,
      "uploadOperations" : [ {
        "method" : "PUT",
        "url" : "https://store-030.blobstore.apple.com/assets/PurpleSource112/v4/8c/be/40/8cbe4070-6a92-e2ac-c88b-65834bf2eab5?uploadId=2bd6bf70-95d6-11f1-b9d8-7e19c51190cb&partNumber=1&Expires=1786488251",
        "length" : 31457280,
        "offset" : 0,
        "requestHeaders" : [ {
          "name" : "Content-Type",
          "value" : "video/mp4"
        } ]
      } ]
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos`

## Request Body

The request body you use to create an app asset library video.

## See Also

- [Modify an app asset library video](patch-v1-appassetlibraryvideos-_id_.md)
  Update an app asset library video.
- [Delete an app asset library video](delete-v1-appassetlibraryvideos-_id_.md)
  Delete an app asset library video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appassetlibraryvideos)*