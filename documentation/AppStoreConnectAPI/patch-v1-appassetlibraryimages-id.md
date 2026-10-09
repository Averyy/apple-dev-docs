# Modify an app asset library image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update an app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing image assets](uploading-and-managing-image-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61

{
  "data": {
    "type": "appAssetLibraryImages",
    "id": "f4000005-e036-8f0b-8018-d259974bee61",
    "attributes": {
      "uploaded": true
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
      "lastModifiedDate" : "2026-08-11T22:44:21Z",
      "fileName" : "menu-screen-6-9.png",
      "fileSize" : 1284736,
      "imageAsset" : null,
      "referenceName" : "Menu screen",
      "specId" : null,
      "state" : "UPLOAD_COMPLETE",
      "stateDetails" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61"
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

The request body you use to update an app asset library image.

## See Also

- [Create an app asset library image](post-v1-appassetlibraryimages.md)
  Create an app asset library image.
- [Delete an app asset library image](delete-v1-appassetlibraryimages-_id_.md)
  Delete an app asset library image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appassetlibraryimages-_id_)*