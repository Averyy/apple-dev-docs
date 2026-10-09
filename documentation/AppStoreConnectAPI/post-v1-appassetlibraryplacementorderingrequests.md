# Create an app asset library placement ordering request

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create an app asset library placement ordering request.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)
- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacementOrderingRequests

{
  "data": {
    "type": "appAssetLibraryPlacementOrderingRequests",
    "attributes": {
      "placementGroup": "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE"
    },
    "relationships": {
      "orderedPlacements": {
        "data": [
          {
            "type": "appAssetLibraryPlacements",
            "id": "1e800005-e036-8f0b-8f37-9c5cc67e23a1"
          },
          {
            "type": "appAssetLibraryPlacements",
            "id": "2e000005-e036-8f0b-8f25-6dbc2baa784a"
          }
        ]
      },
      "appStoreVersionLocalization": {
        "data": {
          "type": "appStoreVersionLocalizations",
          "id": "b3a9b4c2-d2de-43f4-ad8c-71c5ebe301d1"
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
    "type" : "appAssetLibraryPlacementOrderingRequests",
    "id" : "24f44809-07db-497e-8ea9-153baedd0771",
    "relationships" : {
      "orderedPlacements" : {
        "meta" : {
          "paging" : {
            "total" : 2,
            "limit" : 10
          }
        },
        "data" : [ {
          "type" : "appAssetLibraryPlacements",
          "id" : "1e800005-e036-8f0b-8f37-9c5cc67e23a1"
        }, {
          "type" : "appAssetLibraryPlacements",
          "id" : "2e000005-e036-8f0b-8f25-6dbc2baa784a"
        } ]
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacementOrderingRequests/24f44809-07db-497e-8ea9-153baedd0771"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacementOrderingRequests"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appAssetLibraryPlacementOrderingRequests`

## Parameters

- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[orderedPlacements]` (integer): The maximum number of related ordered placement resources to return.
- `fields[appAssetLibraryPlacementOrderingRequests]` ([string]): Additional fields to include for each app asset library placement ordering request resource returned by the response.

## Request Body

The request body you use to create an app asset library placement ordering request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appassetlibraryplacementorderingrequests)*