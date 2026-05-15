# Read Information About the Availablity of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the territory availablity for an in-app purchase.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593
```

**Response**:

```json
  "data" : {
    "type" : "inAppPurchaseAvailabilities",
    "id" : "6447501593",
    "attributes" : {
      "availableInNewTerritories" : false
    },
    "relationships" : {
      "availableTerritories" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593/relationships/availableTerritories",
          "related" : "https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593/availableTerritories"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/{id}`

## Parameters

- `fields[inAppPurchaseAvailabilities]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit[availableTerritories]` (integer)

## See Also

- [List the Territory Availablity of an In-App Purchase](get-v1-inapppurchaseavailabilities-_id_-availableterritories.md)
  List all the territories where an in-app purchase is available.
- [GET /v1/inAppPurchaseAvailabilities/{id}/relationships/availableTerritories](get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories.md)
- [Modify the Territory Availablity of an In-App Purchase](post-v1-inapppurchaseavailabilities.md)
  Update the territory availablity of a specific in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseavailabilities-_id_)*