# List all subscription price ids for an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of resource IDs representing subscription prices for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/prices`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionPricesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting price points and prices
- [List all price points for a subscription](./get-v1-subscriptions-_id_-pricepoints.md)
  Get a list of price points for an auto-renewable subscription by territory.
- [List price point IDs for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-pricepoints.md)
- [List all prices for a subscription](./get-v1-subscriptions-_id_-prices.md)
  Get a list of prices for an auto-renewable subscription, by territory.
- [Delete prices from a subscription](./delete-v1-subscriptions-_id_-relationships-prices.md)
  Delete a scheduled subscription price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-relationships-prices)*