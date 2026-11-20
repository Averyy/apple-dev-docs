# SeatPriceTier

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

A volume price tier for a subscription item that a customer buys as a multiseat purchase.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SeatPriceTier
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)

## Discussion

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

The `seatPriceTiers` array of a [`SubscriptionCreateItem`](./subscriptioncreateitem.md), [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md), or [`SubscriptionPriceChangeItem`](./subscriptionpricechangeitem.md) contains from one to five tiers. A single tier gives every seat the same price, for per-seat pricing. Two or more tiers give volume discount pricing, where the price per seat decreases as the number of seats increases.

Follow these rules when you create the tiers:

- List the tiers in order, from the most expensive price per seat to the least expensive.
- Make the price of each tier lower than the price of the tier before it.
- Provide a `maximumSeatQuantity` for every tier except the last, and omit it for the last tier.

The `maximumSeatQuantity` value is the number of seats in the tier, not the position of the tier’s last seat. Seats fill the tiers in order, starting with the first tier. For example, if the first two tiers each have a `maximumSeatQuantity` of `5`, a purchase of 12 seats includes 5 seats at the first tier’s price, 5 seats at the second tier’s price, and 2 seats at the last tier’s price. To calculate the total for the seats, multiply the price of each tier by the number of seats at that tier, and then add the results.

Provide the complete set of tiers each time you include `seatPriceTiers` in a request, including when you add seats or change the price. For more information, see [Creating multiseat purchases](./creating-multiseat-purchases.md).

## Properties

- `maximumSeatQuantity` (int32): The number of seats in the tier. Omit this value for the last tier, which has no upper limit.

  **Minimum**: `1`
- `price` (price) *(required)*: The price per seat for the tier, in milliunits of the currency.

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
- [object SubscriptionPriceChangeItem](./subscriptionpricechangeitem.md)
  The data your app provides to change a subscription price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/seatpricetier)*