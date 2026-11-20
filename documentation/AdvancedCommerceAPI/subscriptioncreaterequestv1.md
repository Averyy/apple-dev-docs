# SubscriptionCreateRequestV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionCreateRequestV1
```

## Properties

- `currency` (currency) *(required)*
- `descriptors` (Descriptors) *(required)*
- `items` ([SubscriptionCreateItemV1]) *(required)*
- `operation` (string) *(required)*: **Allowed Values**: `CREATE_SUBSCRIPTION`
- `period` (period) *(required)*
- `previousTransactionId` (transactionId)
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode) *(required)*
- `version` (versionV1) *(required)*

## See Also

### Subscription creation in the app
- [object SubscriptionCreateRequest](./subscriptioncreaterequest.md)
  The request data your app provides when a customer purchases an auto-renewable subscription.
- [object SubscriptionCreateItem](./subscriptioncreateitem.md)
  The data that describes a subscription item.
- [object BundleItem](./bundleitem.md)
- [object SubscriptionCreateItemV1](./subscriptioncreateitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreaterequestv1)*