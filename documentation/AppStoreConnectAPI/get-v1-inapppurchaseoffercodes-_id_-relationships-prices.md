# Get All Price IDs for an In-App Purchase Offer Code

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of price resource IDs for a specific In-App Purchase offer code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodes/{id}/relationships/prices`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`InAppPurchaseOfferCodePricesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Managing In-App Purchase Offer Codes
- [Create an In-App Purchase Offer Code](./post-v1-inapppurchaseoffercodes.md)
  Create an offer code for an In-App Purchase.
- [Read In-App Purchase Offer Code Information](./get-v1-inapppurchaseoffercodes-_id_.md)
  Get information about a specific In-App Purchase offer code.
- [Modify an In-App Purchase Offer Code](./patch-v1-inapppurchaseoffercodes-_id_.md)
  Update a specific In-App Purchase offer code.
- [List All Prices for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-prices.md)
  Get a list of prices for a specific In-App Purchase offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseoffercodes-_id_-relationships-prices)*