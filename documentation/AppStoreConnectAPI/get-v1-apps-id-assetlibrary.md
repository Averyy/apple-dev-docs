# Read related asset library

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the asset library for an app.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)
- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)
- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/1234567890/assetLibrary
```

**Response**:

```json
{
  "data" : {
    "type" : "appAssetLibraries",
    "id" : "1234567890",
    "relationships" : {
      "images" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/images",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/images"
        }
      },
      "videos" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/videos",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/videos"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/1234567890/assetLibrary"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/assetLibrary`

## Parameters

- `fields[appAssetLibraries]` ([string]): Additional fields to include for each app asset library resource returned by the response.

## See Also

- [Get the asset library ID for an app](get-v1-apps-_id_-relationships-assetlibrary.md)
  Get the asset library resource ID for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-assetlibrary)*