# Modify the Territory Availablity of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the territory availablity of a specific In-App Purchase.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```
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

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseAvailabilityCreateRequest`

## Responses

- `201` Created (`InAppPurchaseAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read information about the availablity of an In-App Purchase](./get-v1-inapppurchaseavailabilities-_id_.md)
  Get information about the territory availablity for an In-App Purchase.
- [List the Territory Availablity of an In-App Purchase](./get-v1-inapppurchaseavailabilities-_id_-availableterritories.md)
  List all the territories where an In-App Purchase is available.
- [List available territory IDs for an In-App Purchase availability](./get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-inapppurchaseavailabilities)*