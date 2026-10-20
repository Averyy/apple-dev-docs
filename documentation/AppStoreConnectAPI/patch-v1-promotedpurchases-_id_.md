# Modify a promoted In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the visibility of a promoted In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/promotedPurchases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `PromotedPurchaseUpdateRequest`

## Responses

- `200` OK (`PromotedPurchaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Promote a purchase](./post-v1-promotedpurchases.md)
  Add an existing In-App Purchase or auto-renewable subscription to the promoted In-App Purchases on an app listing in the App Store.
- [List all promoted purchases for an app](./get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted In-App Purchases, including promoted auto-renewable subscriptions, for an app.
- [List promoted purchase ids for an app](./get-v1-apps-_id_-relationships-promotedpurchases.md)
  Get a list of resource IDs representing promoted purchases for an auto-renewable subscription.
- [Read promoted purchase information](./get-v1-promotedpurchases-_id_.md)
  Get details about a specific promoted In-App Purchase.
- [Modify the order of a promoted purchase for an app](./patch-v1-apps-_id_-relationships-promotedpurchases.md)
  Update the order of promoted purchases.
- [Remove a promoted purchase](./delete-v1-promotedpurchases-_id_.md)
  Remove a promotion for an In-App Purchase or auto-renewable subscription from the App Store listing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-promotedpurchases-_id_)*