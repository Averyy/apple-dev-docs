# SubscriptionReactivateInAppRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The request your app provides to reactivate a subscription that has automatic renewal turned off.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object SubscriptionReactivateInAppRequest
```

## Properties

- `items` ([SubscriptionReactivateItem])
- `operation` (string) *(required)*
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `transactionId` (transactionId) *(required)*
- `version` (version) *(required)*

## See Also

- [object SubscriptionReactivateItem](subscriptionreactivateitem.md)
  An item in a subscription to reactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest)*