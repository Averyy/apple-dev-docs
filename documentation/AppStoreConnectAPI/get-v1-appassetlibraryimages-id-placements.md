# List related placements

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the placements that reuse an app asset library image.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Migrating to the App Asset Library](migrating-to-the-app-asset-library.md)
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)
- [Uploading and managing image assets](uploading-and-managing-image-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/placements?limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryPlacements",
    "id" : "2e000005-e036-8f0b-8f25-6dbc2baa784a",
    "attributes" : {
      "mediaType" : "IMAGE",
      "placementType" : "APP_SCREENSHOT",
      "placementGroup" : "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE",
      "createdDate" : "2026-08-11T22:45:27Z",
      "lastModifiedDate" : "2026-08-11T22:45:27Z",
      "state" : "PARENT_PREPARE_FOR_SUBMISSION",
      "stateDetails" : null
    },
    "relationships" : {
      "image" : {
        "data" : {
          "type" : "appAssetLibraryImages",
          "id" : "f4000005-e036-8f0b-8018-d259974bee61"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/2e000005-e036-8f0b-8f25-6dbc2baa784a"
    }
  }, {
    "type" : "appAssetLibraryPlacements",
    "id" : "1e800005-e036-8f0b-8f37-9c5cc67e23a1",
    "attributes" : {
      "mediaType" : "IMAGE",
      "placementType" : "IMESSAGE_APP_SCREENSHOT",
      "placementGroup" : "IMESSAGE_IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE",
      "createdDate" : "2026-08-11T22:45:27Z",
      "lastModifiedDate" : "2026-08-11T22:45:27Z",
      "state" : "PARENT_PREPARE_FOR_SUBMISSION",
      "stateDetails" : null
    },
    "relationships" : {
      "image" : {
        "data" : {
          "type" : "appAssetLibraryImages",
          "id" : "f4000005-e036-8f0b-8018-d259974bee61"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/1e800005-e036-8f0b-8f37-9c5cc67e23a1"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/f4000005-e036-8f0b-8018-d259974bee61/placements"
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

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryImages/{id}/placements`

## Parameters

- `filter[placementType]` ([string]): Filter the returned app asset library placements by placement type.
- `filter[placementGroup]` ([string]): Filter the returned app asset library placements by placement group.
- `filter[state]` ([string]): Filter the returned app asset library placements by state.
- `filter[video]` ([string]): Filter the returned app asset library placements by video.
- `filter[appEventLocalization]` ([string]): Filter the returned app asset library placements by in-app event localization.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app asset library placements by App Store version localization.
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app asset library placements by app custom product page localization.
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app asset library placements by App Store version experiment treatment localization.
- `filter[id]` ([string]): Filter the returned app asset library placements by resource ID.
- `sort` ([string]): Attributes by which to sort.
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `fields[appAssetLibraryImages]` ([string]): Additional fields to include for each app asset library image resource returned by the response.
- `fields[appAssetLibraryVideos]` ([string]): Additional fields to include for each app asset library video resource returned by the response.
- `fields[appEventLocalizations]` ([string]): Additional fields to include for each in-app event localization resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `limit` (integer): The maximum number of app asset library placement resources to return.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Read an app asset library image](get-v1-appassetlibraryimages-_id_.md)
  Get information about an app asset library image.
- [List the placement IDs for an app asset library image](get-v1-appassetlibraryimages-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific app asset library image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryimages-_id_-placements)*