# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus

**Framework**: StoreKit  
**Kind**: enum

Status values that indicate whether an auto-renewable subscription is subject to a price increase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum PriceIncreaseStatus
```

#### Overview

For more information, see [`Managing Price Increases for Auto-Renewable Subscriptions`](managing-price-increases-for-auto-renewable-subscriptions.md).

## Topics

### Getting Price Increase Status
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/noincreasepending.md)
  There’s no pending price increase for the auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed.md)
  The auto-renewable subscription is subject to a price increase.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/pending.md)
  The customer hasn’t yet responded to an auto-renewable subscription price increase that requires customer consent.
### Getting a Localized Description
- [var localizedDescription: String](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/localizeddescription.md)
  A string containing the localized description of the price increase status.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Managing Price Increases for Auto-Renewable Subscriptions](managing-price-increases-for-auto-renewable-subscriptions.md)
  Identify the price increase status for auto-renewable subscriptions in your app and on your server.
- [let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.property.md)
  The status that indicates whether the auto-renewable subscription is subject to a price increase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum)*