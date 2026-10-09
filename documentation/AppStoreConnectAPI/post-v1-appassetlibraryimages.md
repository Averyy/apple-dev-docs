# Create an app asset library image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create an app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages

{
  "data": {
    "type": "appAssetLibraryImages",
    "attributes": {
      "fileName": "menu-screen-6-9.png",
      "fileSize": 1284736,
      "category": "APP_SCREENSHOTS_AND_PREVIEWS",
      "referenceName": "Menu screen"
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
    "type" : "appAssetLibraryImages",
    "id" : "f4000005-e036-8f0b-8018-d259974bee61",
    "attributes" : {
      "category" : "APP_SCREENSHOTS_AND_PREVIEWS",
      "createdDate" : "2026-08-11T22:44:12Z",
      "lastModifiedDate" : "2026-08-11T22:44:12Z",
      "fileName" : "menu-screen-6-9.png",
      "fileSize" : 1284736,
      "imageAsset" : null,
      "referenceName" : "Menu screen",
      "specId" : null,
      "state" : "AWAITING_UPLOAD",
      "stateDetails" : null,
      "uploadOperations" : [ {
        "method" : "PUT",
        "url" : "https://store-030.blobstore.apple.com/assets/PurpleSource112/v4/8c/be/40/8cbe4070-6a92-e2ac-c88b-65834bf2eab5?uploadId=2bd6bf70-95d6-11f1-b9d8-7e19c51190cb&partNumber=1&Expires=1786488251",
        "length" : 1284736,
        "offset" : 0,
        "requestHeaders" : [ {
          "name" : "Content-Type",
          "value" : "image/png"
        } ]
      } ]
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages`

## Request Body

The request body you use to create an app asset library image.

## See Also

- [Modify an app asset library image](patch-v1-appassetlibraryimages-_id_.md)
  Update an app asset library image.
- [Delete an app asset library image](delete-v1-appassetlibraryimages-_id_.md)
  Delete an app asset library image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appassetlibraryimages)*