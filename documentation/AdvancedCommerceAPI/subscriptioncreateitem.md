# SubscriptionCreateItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The data that describes a subscription item.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionCreateItem
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md)

## Discussion

### Sell a subscription as a multiseat purchase

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

To sell a subscription item as a multiseat purchase, provide one to five [`SeatPriceTier`](./seatpricetier.md) objects in `seatPriceTiers`, and the number of seats in [`finalQuantity`](./subscriptioncreateitem/finalquantity.md), instead of a `price`. A multiseat subscription contains a single item; the item can’t include `bundleItems`, so you can’t sell a bundle or a suite as a multiseat purchase. For more information, see [Creating multiseat purchases](./creating-multiseat-purchases.md).

## Properties

- `SKU` (SKU) *(required)*: The item’s product identifier, which you define.

  **Maximum Length**: `128`
- `bundleItems` ([BundleItem])
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `finalQuantity` (finalQuantity): The number of seats for an item that a customer buys as a multiseat purchase. Provide it together with `seatPriceTiers`.

  **Minimum**: `1`
- `isUnbundleable` (boolean)
- `offer` (Offer)
- `partners` ([Partner])
- `period` (period)
- `previousTransactionId` (transactionId)
- `price` (price): The price of the item. Provide either `price` or `seatPriceTiers`.
- `seatPriceTiers` ([SeatPriceTier]): The volume price tiers for an item that a customer buys as a multiseat purchase, from the most expensive tier to the least expensive. Provide either `price` or `seatPriceTiers`.
- `taxCode` (taxCode)

## See Also

### Subscription creation in the app
- [object SubscriptionCreateRequest](./subscriptioncreaterequest.md)
  The request data your app provides when a customer purchases an auto-renewable subscription.
- [object BundleItem](./bundleitem.md)
- [object SubscriptionCreateRequestV1](./subscriptioncreaterequestv1.md)
- [object SubscriptionCreateItemV1](./subscriptioncreateitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreateitem)*