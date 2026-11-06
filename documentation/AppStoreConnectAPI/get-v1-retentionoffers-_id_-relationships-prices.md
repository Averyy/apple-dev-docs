# List price IDs for a retention offer

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of price IDs for a specific retention offer.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/retentionOffers/{id}/relationships/prices`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention offer resource ID from the [`List retention offers for a subscription`](./get-v1-subscriptions-_id_-retentionoffers.md) response.

### Query Parameters

- `limit` (integer): The maximum number of price resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`RetentionOfferPricesLinkagesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention offers
- [Read a retention offer](./get-v1-retentionoffers-_id_.md)
  Read details about a specific retention offer.
- [List prices for a retention offer](./get-v1-retentionoffers-_id_-prices.md)
  Get a list of territory-specific prices for a specific retention offer.
- [List retention offers for a subscription](./get-v1-subscriptions-_id_-retentionoffers.md)
  Get a list of all retention offers for a specific auto-renewable subscription.
- [List retention offer IDs for a subscription](./get-v1-subscriptions-_id_-relationships-retentionoffers.md)
  Get a list of retention offer IDs for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-retentionoffers-_id_-relationships-prices)*