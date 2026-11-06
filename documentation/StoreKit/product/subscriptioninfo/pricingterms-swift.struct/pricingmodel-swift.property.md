# pricingModel

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The pricing model of these pricing terms, which is either a single price or seat-based pricing.

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
let pricingModel: Product.SubscriptionInfo.PricingTerms.PricingModel
```

## Mentions

- [Supporting multiseat purchases in your app](../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

A single price applies when a customer buys the subscription individually. Seat-based pricing applies when a customer buys it as a multiseat subscription, and provides a per-seat price for each price tier. For an example that reads the price details, see [`Product.SubscriptionInfo.PricingTerms.PricingModel`](./pricingmodel-swift.enum.md).

## See Also

### Getting the pricing model
- [Product.SubscriptionInfo.PricingTerms.PricingModel](./pricingmodel-swift.enum.md)
  The pricing models of an auto-renewable subscription, with the pricing details for each model.
- [Product.SubscriptionInfo.PricingTerms.SinglePrice](./singleprice.md)
  The price and commitment details of a subscription that has a single price.
- [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing](./seatbasedpricing.md)
  The per-seat price tiers of a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.property)*