# Modify the Territory Availablity of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the territory availablity of a specific in-app purchase.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities -d
{
  "data": {
    "type": "inAppPurchaseAvailabilities",
    "attributes": {
      "availableInNewTerritories": true
    },
    "relationships": {
      "availableTerritories": {
        "data": [
          {
            "type": "territories",
            "id": "USA"
          },
          {
            "type": "territories",
            "id": "CAN"
          },
          {
            "type": "territories",
            "id": "ISL"
          }
        ]
      },
      "inAppPurchase": {
        "data": {
          "id": "6447501593",
          "type": "inAppPurchases"
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
    "type" : "inAppPurchaseAvailabilities",
    "id" : "6447501593",
    "attributes" : {
      "availableInNewTerritories" : true
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
    "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities`

## See Also

- [Read information about the availablity of an in-app purchase](get-v1-inapppurchaseavailabilities-_id_.md)
  Get information about the territory availablity for an in-app purchase.
- [List the Territory Availablity of an In-App Purchase](get-v1-inapppurchaseavailabilities-_id_-availableterritories.md)
  List all the territories where an in-app purchase is available.
- [List available territory IDs for an in-app purchase availability](get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-inapppurchaseavailabilities)*