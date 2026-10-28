# List the Territory Availablity of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all the territories where an In-App Purchase is available.

**Availability**:
- App Store Connect API 2.3+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593/availableTerritories
```

**Response**:

```json
{
  "data" : [ {
    "type" : "territories",
    "id" : "ISL",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/ISL"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6447501593/availableTerritories"
  },
  "meta" : {
    "paging" : {
      "total" : 1,
      "limit" : 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/{id}/availableTerritories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the In-App Purchase resource ID from the [`List all In-App Purchases for an app`](./get-v1-apps-_id_-inapppurchasesv2.md) response.

### Query Parameters

- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`TerritoriesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read information about the availablity of an In-App Purchase](./get-v1-inapppurchaseavailabilities-_id_.md)
  Get information about the territory availablity for an In-App Purchase.
- [List available territory IDs for an In-App Purchase availability](./get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories.md)
- [Modify the Territory Availablity of an In-App Purchase](./post-v1-inapppurchaseavailabilities.md)
  Update the territory availablity of a specific In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseavailabilities-_id_-availableterritories)*