# SubscriptionModifyChangeItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The data your app provides to change an item of an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionModifyChangeItem
```

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `currentSKU` (SKU) *(required)*: **Maximum Length**: `128`
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `effective` (effective) *(required)*
- `offer` (Offer)
- `price` (price) *(required)*
- `proratedPrice` (proratedPrice)
- `reason` (string) *(required)*: **Allowed Values**: `UPGRADE`, `DOWNGRADE`, `APPLY_OFFER`

## See Also

### Subscription modification in the app
- [object SubscriptionModifyInAppRequest](./subscriptionmodifyinapprequest.md)
  The request data your app provides to make changes to an auto-renewable subscription.
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifychangeitem)*