# Read In-App Purchase Offer Code Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific In-App Purchase offer code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodes/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[inAppPurchaseOfferCodeCustomCodes]` ([string]): **Allowed Values**: `customCode`, `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `createdByActor`, `deactivatedByActor`
- `fields[inAppPurchaseOfferCodeOneTimeUseCodes]` ([string]): **Allowed Values**: `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `environment`, `values`, `createdByActor`, `deactivatedByActor`
- `fields[inAppPurchaseOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `productionCodeCount`, `sandboxCodeCount`, `active`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[inAppPurchaseOfferPrices]` ([string]): **Allowed Values**: `territory`, `pricePoint`
- `include` ([string]): **Allowed Values**: `oneTimeUseCodes`, `customCodes`, `prices`
- `limit[customCodes]` (integer): **Maximum**: `50`
- `limit[oneTimeUseCodes]` (integer): **Maximum**: `50`
- `limit[prices]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`InAppPurchaseOfferCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Managing In-App Purchase Offer Codes
- [Create an In-App Purchase Offer Code](./post-v1-inapppurchaseoffercodes.md)
  Create an offer code for an In-App Purchase.
- [Modify an In-App Purchase Offer Code](./patch-v1-inapppurchaseoffercodes-_id_.md)
  Update a specific In-App Purchase offer code.
- [List All Prices for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-prices.md)
  Get a list of prices for a specific In-App Purchase offer code.
- [Get All Price IDs for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific In-App Purchase offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseoffercodes-_id_)*