# Product.SubscriptionInfo.PricingTerms.PricingModel.singlePrice(_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A pricing model that uses a single price for the subscription.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
case singlePrice(Product.SubscriptionInfo.PricingTerms.SinglePrice)
```

## Mentions

- [Supporting multiseat purchases in your app](../../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

A subscription that a customer buys individually uses this pricing model. The associated [`Product.SubscriptionInfo.PricingTerms.SinglePrice`](../singleprice.md) value contains the price, the renewal period, and the commitment details.

## See Also

### Identifying the pricing model
- [case seatBased(Product.SubscriptionInfo.PricingTerms.SeatBasedPricing)](./seatbased%28_%29.md)
  A pricing model that uses per-seat prices from one or more price tiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum/singleprice(_:))*