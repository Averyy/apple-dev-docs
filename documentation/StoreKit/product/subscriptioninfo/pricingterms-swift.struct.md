# Product.SubscriptionInfo.PricingTerms

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The billing plan type, pricing model, and offers for one way of paying for an auto-renewable subscription.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
struct PricingTerms
```

## Overview

A subscription can have more than one set of pricing terms. For example, a yearly subscription can bill up front or monthly, and a subscription that supports multiseat purchases has seat-based pricing terms. Get a subscription’s pricing terms from [`pricingTerms`](./pricingterms-swift.property.md).

To display the price, read [`pricingModel`](./pricingterms-swift.struct/pricingmodel-swift.property.md), which is either a single price or seat-based pricing with one or more price tiers.

## Topics

### Getting the billing plan type
- [let billingPlanType: Product.SubscriptionInfo.BillingPlanType](./pricingterms-swift.struct/billingplantype.md)
### Getting the pricing model
- [let pricingModel: Product.SubscriptionInfo.PricingTerms.PricingModel](./pricingterms-swift.struct/pricingmodel-swift.property.md)
  The pricing model of these pricing terms, which is either a single price or seat-based pricing.
- [Product.SubscriptionInfo.PricingTerms.PricingModel](./pricingterms-swift.struct/pricingmodel-swift.enum.md)
  The pricing models of an auto-renewable subscription, with the pricing details for each model.
- [Product.SubscriptionInfo.PricingTerms.SinglePrice](./pricingterms-swift.struct/singleprice.md)
  The price and commitment details of a subscription that has a single price.
- [Product.SubscriptionInfo.PricingTerms.SeatBasedPricing](./pricingterms-swift.struct/seatbasedpricing.md)
  The per-seat price tiers of a multiseat subscription.
### Getting offers
- [let subscriptionOffers: [Product.SubscriptionOffer]](./pricingterms-swift.struct/subscriptionoffers.md)
- [subscript(offers _: Product.SubscriptionOffer.OfferType) -> [Product.SubscriptionOffer]](./pricingterms-swift.struct/subscript%28offers%29.md)
### Deprecated
- [let billingPrice: Decimal](./pricingterms-swift.struct/billingprice.md)
  The price charged at each billing event, in local currency.
- [let billingDisplayPrice: String](./pricingterms-swift.struct/billingdisplayprice.md)
  A localized string representation of the price charged at each billing event.
- [let billingPeriod: Product.SubscriptionInfo.BillingPeriod](./pricingterms-swift.struct/billingperiod.md)
  The period between renewals.
- [let commitmentInfo: Product.SubscriptionInfo.CommitmentInfo](./pricingterms-swift.struct/commitmentinfo.md)
  The commitment the customer agrees to when they subscribe to the product.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting pricing terms
- [let pricingTerms: [Product.SubscriptionInfo.PricingTerms]](./pricingterms-swift.property.md)
  The pricing terms available for the subscription, including its billing plan types and pricing models.
- [Product.SubscriptionInfo.BillingPlanType](./billingplantype.md)
- [Product.SubscriptionInfo.BillingInfo](./billinginfo.md)
  The price charged at each billing event, and the period between renewals.
- [Product.SubscriptionInfo.BillingPeriod](./billingperiod.md)
- [Product.SubscriptionInfo.CommitmentInfo](./commitmentinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct)*