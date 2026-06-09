# Delete a Win-Back Offer

**Framework**: App Store Connect API  
**Kind**: httpRequest

The data structure that represents a delete-v1-win back offers-{id} resource.

**Availability**:
- App Store Connect API 3.6+

#### Overview

Remove a win-back offer for a specific subscription.

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
  The data structure that represents a get-v1-subscriptions-{id}-win back offers resource.
- [List win-back offer IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [Read Win-Back Offer Information](get-v1-winbackoffers-_id_.md)
  The data structure that represents a get-v1-win back offers-{id} resource.
- [List Win-Back Offer Prices](get-v1-winbackoffers-_id_-prices.md)
  The data structure that represents a get-v1-win back offers-{id}-prices resource.
- [List price IDs for a win-back offer](get-v1-winbackoffers-_id_-relationships-prices.md)
- [Create a Win-Back Offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a Win-Back Offer](patch-v1-winbackoffers-_id_.md)
  The data structure that represents a patch-v1-win back offers-{id} resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-winbackoffers-_id_)*