# SubscriptionReactivateItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An item in a subscription to reactivate.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object SubscriptionReactivateItem
```

## Discussion

This object is part of the [`SubscriptionReactivateInAppRequest`](./subscriptionreactivateinapprequest.md) that your app uses to reactivate a subscription that would otherwise expire.

## Properties

- `SKU` (SKU) *(required)*: The SKU of the item to reactivate.

  **Maximum Length**: `128`

## See Also

### Subscription reactivation in the app
- [object SubscriptionReactivateInAppRequest](./subscriptionreactivateinapprequest.md)
  The request your app provides to reactivate a subscription that has automatic renewal turned off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateitem)*