# List related images

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the image assets in an app’s asset library.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/images?filter[state]=PREPARE_FOR_SUBMISSION&sort=-createdDate&limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryImages",
    "id" : "c3000005-e036-8f0b-8038-36fbc8d1c4ae",
    "attributes" : {
      "category" : "APP_SCREENSHOTS_AND_PREVIEWS",
      "createdDate" : "2026-08-11T22:47:02Z",
      "lastModifiedDate" : "2026-08-11T22:47:19Z",
      "fileName" : "order-screen-6-9.png",
      "fileSize" : 1284736,
      "imageAsset" : {
        "templateUrl" : "https://is1.mzstatic.com/image/thumb/AOsFKpK1JfF_vrxSCSbIew/{w}x{h}bb.{f}",
        "width" : 1290,
        "height" : 2796
      },
      "referenceName" : "Order screen",
      "specId" : "f56c777c-99ea-5760-97ae-27c5f8cbb884",
      "state" : "PREPARE_FOR_SUBMISSION",
      "stateDetails" : null
    },
    "relationships" : {
      "placements" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/c3000005-e036-8f0b-8038-36fbc8d1c4ae/relationships/placements",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/c3000005-e036-8f0b-8038-36fbc8d1c4ae/placements"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/c3000005-e036-8f0b-8038-36fbc8d1c4ae"
    }
  }, {
    "type" : "appAssetLibraryImages",
    "id" : "f4000005-e036-8f0b-8018-d259974bee61",
    "attributes" : {
      "category" : "APP_SCREENSHOTS_AND_PREVIEWS",
      "createdDate" : "2026-08-11T22:44:12Z",
      "lastModifiedDate" : "2026-08-11T22:44:31Z",
      "fileName" : "menu-screen-6-9.png",
      "fileSize" : 1284736,
      "imageAsset" : {
        "templateUrl" : "https://is1.mzstatic.com/image/thumb/AOsFKpK1JfF_vrxSCSbIew/{w}x{h}bb.{f}",
        "width" : 1290,
        "height" : 2796
      },
      "referenceName" : "Menu screen",
      "specId" : "f56c777c-99ea-5760-97ae-27c5f8cbb884",
      "state" : "PREPARE_FOR_SUBMISSION",
      "stateDetails" : null
    },
    "relationships" : {
      "placements" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/relationships/placements",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/placements"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/images"
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

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraries/{id}/images`

## Parameters

- `filter[category]` ([string]): Filter the returned app asset library images by category.
- `filter[state]` ([string]): Filter the returned app asset library images by state.
- `filter[referenceName]` ([string]): Filter the returned app asset library images by reference name.
- `filter[specId]` ([string]): Filter the returned app asset library images by specification ID.
- `filter[id]` ([string]): Filter the returned app asset library images by resource ID.
- `sort` ([string]): Attributes by which to sort.
- `fields[appAssetLibraryImages]` ([string]): Additional fields to include for each app asset library image resource returned by the response.
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `limit` (integer): The maximum number of app asset library image resources to return.
- `include` ([string]): The relationship data to include in the response.
- `limit[placements]` (integer): The maximum number of related placement resources to return.

## See Also

- [List related videos](get-v1-appassetlibraries-_id_-videos.md)
  List the video assets in an app’s asset library.
- [List the image IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-images.md)
  Get a list of image asset resource IDs for a specific asset library.
- [List the video IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-videos.md)
  Get a list of video asset resource IDs for a specific asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraries-_id_-images)*