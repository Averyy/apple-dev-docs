# commitmentInfo

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The commitment the customer agrees to when they subscribe to the product.

**Availability**:
- iOS 26.4+ - Deprecated in 27.3
- iPadOS 26.4+ - Deprecated in 27.3
- Mac Catalyst 26.4+ - Deprecated in 27.3
- macOS 26.4+ - Deprecated in 27.3
- tvOS 26.4+ - Deprecated in 27.3
- visionOS 26.4+ - Deprecated in 27.3
- watchOS 26.4+ - Deprecated in 27.3

> **Deprecated**: Use [`pricingModel`](./pricingmodel-swift.property.md) instead.

## Declaration

```swift
let commitmentInfo: Product.SubscriptionInfo.CommitmentInfo
```

## Mentions

- [Supporting monthly subscriptions with a 12-month commitment](../../../supporting-monthly-subscriptions-with-a-12-month-commitment.md)

## See Also

### Deprecated
- [let billingPrice: Decimal](./billingprice.md)
  The price charged at each billing event, in local currency.
- [let billingDisplayPrice: String](./billingdisplayprice.md)
  A localized string representation of the price charged at each billing event.
- [let billingPeriod: Product.SubscriptionInfo.BillingPeriod](./billingperiod.md)
  The period between renewals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/commitmentinfo)*