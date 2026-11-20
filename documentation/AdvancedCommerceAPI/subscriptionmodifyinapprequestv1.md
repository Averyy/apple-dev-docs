# SubscriptionModifyInAppRequestV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionModifyInAppRequestV1
```

## Properties

- `addItems` ([SubscriptionModifyAddItem])
- `changeItems` ([SubscriptionModifyChangeItemV1])
- `currency` (currency)
- `descriptors` (SubscriptionModifyDescriptors)
- `operation` (string) *(required)*: **Allowed Values**: `MODIFY_SUBSCRIPTION`
- `periodChange` (SubscriptionModifyPeriodChange)
- `removeItems` ([SubscriptionModifyRemoveItem])
- `requestInfo` (RequestInfo) *(required)*
- `retainBillingCycle` (retainBillingCycle) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode)
- `transactionId` (transactionId) *(required)*
- `version` (versionV1) *(required)*

## See Also

### Subscription modification in the app
- [object SubscriptionModifyInAppRequest](./subscriptionmodifyinapprequest.md)
  The request data your app provides to make changes to an auto-renewable subscription.
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](./subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object ModifyBundleItem](./modifybundleitem.md)
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyChangeItemV1](./subscriptionmodifychangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyinapprequestv1)*