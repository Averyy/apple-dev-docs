# Read an app asset library image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing image assets](uploading-and-managing-image-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61
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
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/{id}`

## Parameters

- `fields[appAssetLibraryImages]` ([string]): Additional fields to include for each app asset library image resource returned by the response.
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[placements]` (integer): The maximum number of related placement resources to return.

## See Also

- [List related placements](get-v1-appassetlibraryimages-_id_-placements.md)
  List the placements that reuse an app asset library image.
- [List the placement IDs for an app asset library image](get-v1-appassetlibraryimages-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific app asset library image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryimages-_id_)*