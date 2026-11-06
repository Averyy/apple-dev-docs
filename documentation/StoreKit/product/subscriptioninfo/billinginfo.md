# Product.SubscriptionInfo.BillingInfo

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The price charged at each billing event, and the period between renewals.

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
struct BillingInfo
```

## Topics

### Getting the price
- [let price: Decimal](./billinginfo/price.md)
  The price charged at each billing event, in local currency.
- [let displayPrice: String](./billinginfo/displayprice.md)
  A localized string representation of the price charged at each billing event.
### Getting the renewal period
- [let period: Product.SubscriptionInfo.BillingPeriod](./billinginfo/period.md)
  The period between renewals of the subscription.

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
- [Product.SubscriptionInfo.PricingTerms](./pricingterms-swift.struct.md)
  The billing plan type, pricing model, and offers for one way of paying for an auto-renewable subscription.
- [Product.SubscriptionInfo.BillingPlanType](./billingplantype.md)
- [Product.SubscriptionInfo.BillingPeriod](./billingperiod.md)
- [Product.SubscriptionInfo.CommitmentInfo](./commitmentinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/billinginfo)*