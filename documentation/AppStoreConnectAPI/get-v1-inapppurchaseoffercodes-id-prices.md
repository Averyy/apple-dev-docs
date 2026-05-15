# List All Prices for an In-App Purchase Offer Code

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of prices for a specific in-app purchase offer code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodes/{id}/prices`

## Parameters

- `fields[inAppPurchaseOfferPrices]` ([string])
- `fields[inAppPurchasePricePoints]` ([string])
- `fields[territories]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Create an In-App Purchase Offer Code](post-v1-inapppurchaseoffercodes.md)
  Create an offer code for an in-app purchase.
- [Read In-App Purchase Offer Code Information](get-v1-inapppurchaseoffercodes-_id_.md)
  Get information about a specific in-app purchase offer code.
- [Modify an In-App Purchase Offer Code](patch-v1-inapppurchaseoffercodes-_id_.md)
  Update a specific in-app purchase offer code.
- [Get All Price IDs for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific in-app purchase offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseoffercodes-_id_-prices)*