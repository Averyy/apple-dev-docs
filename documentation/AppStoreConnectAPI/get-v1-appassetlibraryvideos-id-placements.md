# List related placements

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the placements that reuse an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Uploading and managing video assets](uploading-and-managing-video-assets.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/placements?limit=1
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appAssetLibraryPlacements",
    "id" : "2e000005-e036-8f0b-8f25-6dbc2baa784a",
    "attributes" : {
      "mediaType" : "VIDEO",
      "placementType" : "APP_PREVIEW",
      "placementGroup" : "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE",
      "createdDate" : "2026-08-11T22:45:27Z",
      "lastModifiedDate" : "2026-08-11T22:45:27Z",
      "state" : "PARENT_PREPARE_FOR_SUBMISSION",
      "stateDetails" : null
    },
    "relationships" : {
      "video" : {
        "data" : {
          "type" : "appAssetLibraryVideos",
          "id" : "3b100005-e036-8f0b-8021-77aa41c6b502"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacements/2e000005-e036-8f0b-8f25-6dbc2baa784a"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/3b100005-e036-8f0b-8021-77aa41c6b502/placements"
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

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryVideos/{id}/placements`

## Parameters

- `filter[placementType]` ([string]): Filter the returned app asset library placements by placement type.
- `filter[placementGroup]` ([string]): Filter the returned app asset library placements by placement group.
- `filter[state]` ([string]): Filter the returned app asset library placements by state.
- `filter[image]` ([string]): Filter the returned app asset library placements by image.
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

- [Read an app asset library video](get-v1-appassetlibraryvideos-_id_.md)
  Get information about an app asset library video.
- [List the placement IDs for an app asset library video](get-v1-appassetlibraryvideos-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific app asset library video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryvideos-_id_-placements)*