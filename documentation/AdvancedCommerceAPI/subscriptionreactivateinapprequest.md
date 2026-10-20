# SubscriptionReactivateInAppRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request your app provides to reactivate a subscription that has automatic renewal turned off.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object SubscriptionReactivateInAppRequest
```

## Properties

- `items` ([SubscriptionReactivateItem])
- `operation` (string) *(required)*: **Allowed Values**: `REACTIVATE_SUBSCRIPTION`
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `transactionId` (transactionId) *(required)*
- `version` (version) *(required)*

## See Also

### Subscription reactivation in the app
- [object SubscriptionReactivateItem](./subscriptionreactivateitem.md)
  An item in a subscription to reactivate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest)*