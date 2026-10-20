# List available territory IDs for an In-App Purchase availability

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/{id}/relationships/availableTerritories`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read information about the availablity of an In-App Purchase](./get-v1-inapppurchaseavailabilities-_id_.md)
  Get information about the territory availablity for an In-App Purchase.
- [List the Territory Availablity of an In-App Purchase](./get-v1-inapppurchaseavailabilities-_id_-availableterritories.md)
  List all the territories where an In-App Purchase is available.
- [Modify the Territory Availablity of an In-App Purchase](./post-v1-inapppurchaseavailabilities.md)
  Update the territory availablity of a specific In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseavailabilities-_id_-relationships-availableterritories)*