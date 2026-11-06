# pricingTerms

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The pricing terms available for the subscription, including its billing plan types and pricing models.

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
let pricingTerms: [Product.SubscriptionInfo.PricingTerms]
```

## Mentions

- [Supporting monthly subscriptions with a 12-month commitment](../../supporting-monthly-subscriptions-with-a-12-month-commitment.md)
- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

Each element describes one set of terms, with its [`billingPlanType`](./pricingterms-swift.struct/billingplantype.md) and its [`pricingModel`](./pricingterms-swift.struct/pricingmodel-swift.property.md). A subscription that customers can buy as a multiseat subscription includes seat-based pricing terms. For more information about billing plan types, see [Supporting monthly subscriptions with a 12-month commitment](../../supporting-monthly-subscriptions-with-a-12-month-commitment.md).

## See Also

### Getting pricing terms
- [Product.SubscriptionInfo.PricingTerms](./pricingterms-swift.struct.md)
  The billing plan type, pricing model, and offers for one way of paying for an auto-renewable subscription.
- [Product.SubscriptionInfo.BillingPlanType](./billingplantype.md)
- [Product.SubscriptionInfo.BillingInfo](./billinginfo.md)
  The price charged at each billing event, and the period between renewals.
- [Product.SubscriptionInfo.BillingPeriod](./billingperiod.md)
- [Product.SubscriptionInfo.CommitmentInfo](./commitmentinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.property)*