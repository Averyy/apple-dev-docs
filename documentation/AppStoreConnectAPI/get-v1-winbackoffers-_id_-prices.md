# List Win-Back Offer Prices

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

The data structure that represents a get-v1-win back offers-{id}-prices resource.

**Availability**:
- App Store Connect API 3.6+

## Overview

List all prices for specific win-back offers.

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/prices
```

**Response**:

```json
{
  "data": [
    {
      "type": "winBackOfferPrices",
      "id": "eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiQ0FOIiwicCI6IjEwMTQyIn0",
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/winBackOfferPrices/eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiQ0FOIiwicCI6IjEwMTQyIn0"
      }
    },
    {
      "type": "winBackOfferPrices",
      "id": "eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiVVNBIiwicCI6IjEwMTI3In0",
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/winBackOfferPrices/eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiVVNBIiwicCI6IjEwMTI3In0"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/prices"
  },
  "meta": {
    "paging": {
      "total": 2,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/winBackOffers/{id}/prices`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `winBackOffers` resource ID from the [`List Win-Back Offers`](./get-v1-subscriptions-_id_-winbackoffers.md) response.

### Query Parameters

- `fields[subscriptionPricePoints]` ([string]): **Allowed Values**: `customerPrice`, `proceeds`, `proceedsYear2`, `territory`, `equalizations`, `adjustedEqualizations`
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `fields[winBackOfferPrices]` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `filter[territory]` ([string])
- `include` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`WinBackOfferPricesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Creating and configuring win-back offers](./creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List Win-Back Offers](./get-v1-subscriptions-_id_-winbackoffers.md)
  The data structure that represents a get-v1-subscriptions-{id}-win back offers resource.
- [List win-back offer IDs for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [Read Win-Back Offer Information](./get-v1-winbackoffers-_id_.md)
  The data structure that represents a get-v1-win back offers-{id} resource.
- [List price IDs for a win-back offer](./get-v1-winbackoffers-_id_-relationships-prices.md)
- [Create a Win-Back Offer](./post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a Win-Back Offer](./patch-v1-winbackoffers-_id_.md)
  The data structure that represents a patch-v1-win back offers-{id} resource.
- [Delete a Win-Back Offer](./delete-v1-winbackoffers-_id_.md)
  The data structure that represents a delete-v1-win back offers-{id} resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-winbackoffers-_id_-prices)*