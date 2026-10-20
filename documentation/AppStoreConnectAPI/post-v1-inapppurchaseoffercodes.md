# Create an In-App Purchase Offer Code

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create an offer code for an In-App Purchase.

**Availability**:
- App Store Connect API 4.2+

## Mentions

- [App Store Connect API 4.2 release notes](./app-store-connect-api-4-2-release-notes.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodes`

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseOfferCodeCreateRequest`

## Responses

- `201` Created (`InAppPurchaseOfferCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Managing In-App Purchase Offer Codes
- [Read In-App Purchase Offer Code Information](./get-v1-inapppurchaseoffercodes-_id_.md)
  Get information about a specific In-App Purchase offer code.
- [Modify an In-App Purchase Offer Code](./patch-v1-inapppurchaseoffercodes-_id_.md)
  Update a specific In-App Purchase offer code.
- [List All Prices for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-prices.md)
  Get a list of prices for a specific In-App Purchase offer code.
- [Get All Price IDs for an In-App Purchase Offer Code](./get-v1-inapppurchaseoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific In-App Purchase offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-inapppurchaseoffercodes)*