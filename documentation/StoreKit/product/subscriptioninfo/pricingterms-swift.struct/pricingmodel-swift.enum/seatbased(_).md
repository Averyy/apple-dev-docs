# Product.SubscriptionInfo.PricingTerms.PricingModel.seatBased(_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A pricing model that uses per-seat prices from one or more price tiers.

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
case seatBased(Product.SubscriptionInfo.PricingTerms.SeatBasedPricing)
```

## Mentions

- [Supporting multiseat purchases in your app](../../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

A subscription that’s enabled for multiseat purchases uses this pricing model when a customer buys it with seats. The associated [`Product.SubscriptionInfo.PricingTerms.SeatBasedPricing`](../seatbasedpricing.md) value contains the price tiers, each with a per-seat price for a range of seats.

## See Also

### Identifying the pricing model
- [case singlePrice(Product.SubscriptionInfo.PricingTerms.SinglePrice)](./singleprice%28_%29.md)
  A pricing model that uses a single price for the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum/seatbased(_:))*