# Delete a Win-Back Offer

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a win-back offer for a specific subscription.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

**Request**:

```html
DELETE https://api.appstoreconnect.apple.com/v1/winBackOffers/10759170294
```

**Response**:

```json
    204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/winBackOffers/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `winBackOffers` resource ID from the [`List Win-Back Offers`](get-v1-subscriptions-_id_-winbackoffers.md) response.

## See Also

- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List Win-Back Offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [GET /v1/subscriptions/{id}/relationships/winBackOffers](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [Read Win-Back Offer Information](get-v1-winbackoffers-_id_.md)
  Read details about a specific win-back offer.
- [List Win-Back Offer Prices](get-v1-winbackoffers-_id_-prices.md)
  List all prices for specific win-back offers.
- [GET /v1/winBackOffers/{id}/relationships/prices](get-v1-winbackoffers-_id_-relationships-prices.md)
- [Create a Win-Back Offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a Win-Back Offer](patch-v1-winbackoffers-_id_.md)
  Edit details for a specific win-back offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-winbackoffers-_id_)*