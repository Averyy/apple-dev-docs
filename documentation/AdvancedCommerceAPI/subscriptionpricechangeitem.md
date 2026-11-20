# SubscriptionPriceChangeItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The data your app provides to change a subscription price.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionPriceChangeItem
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

To change the price of a subscription item that a customer buys as a multiseat purchase, provide the complete set of new [`SeatPriceTier`](./seatpricetier.md) objects in `seatPriceTiers` instead of a `price`; a request with a `price` fails with [`SeatPriceTiersRequiredError`](./seatpricetiersrequirederror.md). The new tiers replace all of the item’s existing tiers. A price change doesn’t change the number of seats.

Whether the change is a price increase depends on the change to the total price of the group purchaser’s seats, and the usual rules for price changes apply. For more information, see [Handling subscription price changes](./handling-subscription-price-changes.md).

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `price` (price): The new price of the item. Provide either `price` or `seatPriceTiers`.
- `seatPriceTiers` ([SeatPriceTier]): The new volume price tiers for an item that a customer buys as a multiseat purchase, from the most expensive tier to the least expensive. Provide either `price` or `seatPriceTiers`.

## See Also

### Objects
- [object Descriptors](./descriptors.md)
  The display name and description of a subscription product.
- [object Offer](./offer.md)
  A discount offer for an auto-renewable subscription.
- [object OfferV1](./offerv1.md)
- [object Partner](./partner.md)
  The identifier and name of a mini app partner associated with a purchase.
- [object RequestInfo](./requestinfo.md)
  The metadata to include in server requests.
- [object SeatPriceTier](./seatpricetier.md)
  A volume price tier for a subscription item that a customer buys as a multiseat purchase.
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](./subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object SubscriptionModifyDescriptors](./subscriptionmodifydescriptors.md)
  The data your app provides to change the description and display name of an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangeitem)*