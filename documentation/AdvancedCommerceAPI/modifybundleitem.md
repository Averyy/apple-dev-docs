# ModifyBundleItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object ModifyBundleItem
```

## Properties

- `SKU` (SKU): **Maximum Length**: `128`
- `appAppleId` (int64)
- `appleProductId` (string)
- `currentSKU` (SKU) *(required)*: **Maximum Length**: `128`
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `previousTransactionId` (transactionId)
- `price` (price) *(required)*
- `taxCode` (taxCode)

## See Also

### Subscription modification in the app
- [object SubscriptionModifyInAppRequest](./subscriptionmodifyinapprequest.md)
  The request data your app provides to make changes to an auto-renewable subscription.
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](./subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyInAppRequestV1](./subscriptionmodifyinapprequestv1.md)
- [object SubscriptionModifyChangeItemV1](./subscriptionmodifychangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/modifybundleitem)*