# List all subscription offer code prices

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of price tiers for a subscription offer code.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}/prices`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionOfferCodePrices]` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `fields[subscriptionPricePoints]` ([string]): **Allowed Values**: `customerPrice`, `proceeds`, `proceedsYear2`, `territory`, `equalizations`, `adjustedEqualizations`
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `include` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `limit` (integer): **Maximum**: `200`
- `filter[territory]` ([string])

## Responses

- `200` OK (`SubscriptionOfferCodePricesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Managing Subscription Offers
- [Create a subscription offer](./post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Read subscription offer code information](./get-v1-subscriptionoffercodes-_id_.md)
  Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.
- [Deactivate a subscription offer with offer codes](./patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List price IDs for a subscription offer code](./get-v1-subscriptionoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific subscription offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_-prices)*