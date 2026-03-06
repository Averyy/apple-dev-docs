# List win-back offer prices

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all prices for specific win-back offers.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[subscriptionPricePoints]` ([string])
- `fields[territories]` ([string])
- `fields[winBackOfferPrices]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List win-back offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [GET /v1/subscriptions/{id}/relationships/winBackOffers](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [Read win-back offer information](get-v1-winbackoffers-_id_.md)
  Read details about a specific win-back offer.
- [GET /v1/winBackOffers/{id}/relationships/prices](get-v1-winbackoffers-_id_-relationships-prices.md)
- [Create a win-back offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a win-back offer](patch-v1-winbackoffers-_id_.md)
  Edit details for a specific win-back offer.
- [Delete a win-back offer](delete-v1-winbackoffers-_id_.md)
  Remove a win-back offer for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-winbackoffers-_id_-prices)*