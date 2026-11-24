# SubscriptionModifyChangeItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The data your app provides to change an item of an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionModifyChangeItem
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)

## Discussion

### Add seats to a multiseat purchase

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

To add seats to a subscription item that a customer buys as a multiseat purchase, send a [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) that meets these conditions:

- The request’s [`effective`](./effective.md) value is `IMMEDIATELY`, because seats you add take effect immediately.
- The change item identifies the item by its `currentSKU`, omits `SKU`, and re-declares the item’s current values, including its `seatPriceTiers` and `period`.
- The change item’s `finalQuantity` contains the total number of seats after the addition, which needs to be higher than the item’s current number of seats.

Make adding seats the only change in the request, and submit other changes, such as a new SKU or period, in a separate request.

A change item can’t reduce the number of seats, and it can’t replace the item’s `seatPriceTiers` with a `price`. The group purchaser reduces the number of seats in their subscription settings, and the change takes effect at the next renewal date. To revoke unclaimed seats, call the [`Revoke Subscription`](./revoke-subscription.md) endpoint with a [`revokeSeatQuantity`](./revokeseatquantity.md). For more information, see [Creating multiseat purchases](./creating-multiseat-purchases.md).

## Properties

- `SKU` (SKU): A new SKU for the item. Omit this value to keep the `currentSKU`, for example when you add seats. When you provide it, it needs to differ from the `currentSKU`.

  **Maximum Length**: `128`
- `bundleItems` ([ModifyBundleItem])
- `currentSKU` (SKU) *(required)*: The item’s current SKU.

  **Maximum Length**: `128`
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `finalQuantity` (finalQuantity): The total number of seats for an item that a customer buys as a multiseat purchase, after the change. Provide it together with `seatPriceTiers`.

  **Minimum**: `1`
- `offer` (Offer)
- `partners` ([Partner])
- `period` (period) *(required)*
- `price` (price): The price of the item. Provide either `price` or `seatPriceTiers`.
- `seatPriceTiers` ([SeatPriceTier]): The volume price tiers for an item that a customer buys as a multiseat purchase, from the most expensive tier to the least expensive. Provide either `price` or `seatPriceTiers`.
- `taxCode` (taxCode) *(required)*
- `transactionId` (transactionId)

## See Also

### Subscription modification in the app
- [object SubscriptionModifyInAppRequest](./subscriptionmodifyinapprequest.md)
  The request data your app provides to make changes to an auto-renewable subscription.
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object ModifyBundleItem](./modifybundleitem.md)
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyInAppRequestV1](./subscriptionmodifyinapprequestv1.md)
- [object SubscriptionModifyChangeItemV1](./subscriptionmodifychangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifychangeitem)*