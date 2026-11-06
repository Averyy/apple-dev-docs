# Product.SubscriptionInfo.PricingTerms.PricingModel

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The pricing models of an auto-renewable subscription, with the pricing details for each model.

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
enum PricingModel
```

## Overview

Switch over a pricing model to get a subscription’s pricing details. A subscription that a customer buys individually uses the [`Product.SubscriptionInfo.PricingTerms.PricingModel.singlePrice(_:)`](./pricingmodel-swift.enum/singleprice%28_%29.md) model. A subscription that a customer buys with seats uses the [`Product.SubscriptionInfo.PricingTerms.PricingModel.seatBased(_:)`](./pricingmodel-swift.enum/seatbased%28_%29.md) model, which provides a per-seat price for each price tier.

StoreKit might add pricing models in the future, so include an `@unknown default` case when you switch over a pricing model.

The following example builds a price label for single-price terms, and a label for each price tier of seat-based terms:

```swift
var priceLabel = ""
var tierLabels: [String] = []

switch pricingTerms.pricingModel {
case .singlePrice(let singlePrice):
    priceLabel = singlePrice.billingInfo.displayPrice
case .seatBased(let seatBasedPricing):
    tierLabels = seatBasedPricing.priceTiers.map { tier in
        let seats = tier.maximumSeats.map { "\(tier.minimumSeats)-\($0)" } ?? "\(tier.minimumSeats)+"
        return "\(seats) seats: \(tier.billingInfo.displayPrice) per seat"
    }
@unknown default:
    break
}
```

For more information, see [Supporting multiseat purchases in your app](../../../supporting-multiseat-purchases-in-your-app.md).

## Topics

### Identifying the pricing model
- [case singlePrice(Product.SubscriptionInfo.PricingTerms.SinglePrice)](./pricingmodel-swift.enum/singleprice%28_%29.md)
  A pricing model that uses a single price for the subscription.
- [case seatBased(Product.SubscriptionInfo.PricingTerms.SeatBasedPricing)](./pricingmodel-swift.enum/seatbased%28_%29.md)
  A pricing model that uses per-seat prices from one or more price tiers.

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
- [Product.SubscriptionInfo.PricingTerms.SinglePrice](./singleprice.md)
  The price and commitment details of a subscription that has a single price.
- [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing](./seatbasedpricing.md)
  The per-seat price tiers of a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum)*