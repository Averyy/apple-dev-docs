# Product.SubscriptionInfo.PricingTerms.SeatBasedPricing

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The per-seat price tiers of a multiseat subscription.

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
struct SeatBasedPricing
```

## Overview

A subscription with per-seat pricing has one price tier. A subscription with volume discount pricing has up to five price tiers, so you can charge less per seat as the number of seats grows. Get the tiers from [`priceTiers`](./seatbasedpricing/pricetiers.md).

For more information, see [Supporting multiseat purchases in your app](../../../supporting-multiseat-purchases-in-your-app.md).

## Topics

### Getting the price tiers
- [let priceTiers: [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier]](./seatbasedpricing/pricetiers.md)
  The price tiers of the subscription, in ascending order of seat count.
- [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing.PriceTier](./seatbasedpricing/pricetier.md)
  A per-seat price that applies to a range of seats.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Getting the pricing model
- [let pricingModel: Product.SubscriptionInfo.PricingTerms.PricingModel](./pricingmodel-swift.property.md)
  The pricing model of these pricing terms, which is either a single price or seat-based pricing.
- [Product.SubscriptionInfo.PricingTerms.PricingModel](./pricingmodel-swift.enum.md)
  The pricing models of an auto-renewable subscription, with the pricing details for each model.
- [Product.SubscriptionInfo.PricingTerms.SinglePrice](./singleprice.md)
  The price and commitment details of a subscription that has a single price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing)*