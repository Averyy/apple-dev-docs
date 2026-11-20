# SubscriptionReactivateInAppRequestV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionReactivateInAppRequestV1
```

## Properties

- `items` ([SubscriptionReactivateItem])
- `operation` (string) *(required)*: **Allowed Values**: `REACTIVATE_SUBSCRIPTION`
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `transactionId` (transactionId) *(required)*
- `version` (versionV1) *(required)*

## See Also

### Subscription reactivation in the app
- [object SubscriptionReactivateInAppRequest](./subscriptionreactivateinapprequest.md)
  The request your app provides to reactivate a subscription that has automatic renewal turned off.
- [object SubscriptionReactivateItem](./subscriptionreactivateitem.md)
  An item in a subscription to reactivate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequestv1)*