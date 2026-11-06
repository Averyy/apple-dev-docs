# Product.SubscriptionInfo.PricingTerms.SinglePrice

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The price and commitment details of a subscription that has a single price.

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
struct SinglePrice
```

## Overview

A subscription that a customer buys individually uses this pricing model.

## Topics

### Getting the price details
- [let billingInfo: Product.SubscriptionInfo.BillingInfo](./singleprice/billinginfo.md)
  The price charged at each billing event, and the period between renewals.
- [let commitmentInfo: Product.SubscriptionInfo.CommitmentInfo](./singleprice/commitmentinfo.md)
  The commitment details of the subscription, including the total price across the commitment period.

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
- [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing](./seatbasedpricing.md)
  The per-seat price tiers of a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/singleprice)*