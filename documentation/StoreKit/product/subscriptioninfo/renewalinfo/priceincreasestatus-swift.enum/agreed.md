# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed

**Framework**: StoreKit  
**Kind**: case

The auto-renewable subscription is subject to a price increase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case agreed
```

## Mentions

- [Managing Price Increases for Auto-Renewable Subscriptions](managing-price-increases-for-auto-renewable-subscriptions.md)

#### Discussion

There are two types of price increases for auto-renewable subscriptions: those that require customer consent, and those that don’t require customer consent. For a price increase that requires customer consent, this value indicates that the customer consented to the price increase. For a price increase that doesn’t require customer consent, this value indicates that the App Store informed the customer of the price increase and the subscription is subject to the price increase.

For more information about this value, see [`Managing Price Increases for Auto-Renewable Subscriptions`](managing-price-increases-for-auto-renewable-subscriptions.md).

## See Also

- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/noincreasepending.md)
  There’s no pending price increase for the auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/pending.md)
  The customer hasn’t yet responded to an auto-renewable subscription price increase that requires customer consent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed)*