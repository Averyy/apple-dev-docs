# SubscriptionPriceChangeRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The request body you use to change the price of an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object SubscriptionPriceChangeRequest
```

##### Discussion

This is the request body for the [`Change Subscription Price`](change-subscription-price.md) endpoint.

The items array contains [`SubscriptionPriceChangeItem`](subscriptionpricechangeitem.md). Include one entry for each SKU within the subscription that has a price change.

## See Also

- [Change Subscription Price](change-subscription-price.md)
  Increase or decrease the price of an auto-renewable subscription, a bundle, or individual items within a subscription at the next renewal.
- [object SubscriptionPriceChangeResponse](subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangerequest)*