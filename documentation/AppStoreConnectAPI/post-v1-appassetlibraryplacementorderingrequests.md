# Create an app asset library placement ordering request

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create an app asset library placement ordering request.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](./app-store-connect-api-4-5-1-release-notes.md)
- [Placing assets on your App Store surfaces](./placing-assets-on-your-app-store-surfaces.md)

#### Discussion

##### Example Request and Response

**Request**:

```
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

### Query Parameters

- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.

  **Allowed Values**: `mediaType`, `placementType`, `placementGroup`, `createdDate`, `lastModifiedDate`, `state`, `stateDetails`, `image`, `video`, `appEventLocalization`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `orderedPlacements`
- `limit[orderedPlacements]` (integer): The maximum number of related ordered placement resources to return.

  **Maximum**: `50`
- `fields[appAssetLibraryPlacementOrderingRequests]` ([string]): Additional fields to include for each app asset library placement ordering request resource returned by the response.

  **Allowed Values**: `orderedPlacements`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppAssetLibraryPlacementOrderingRequestCreateRequest`

The request body you use to create an app asset library placement ordering request.

## Responses

- `201` Created (`AppAssetLibraryPlacementOrderingRequestResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appassetlibraryplacementorderingrequests)*