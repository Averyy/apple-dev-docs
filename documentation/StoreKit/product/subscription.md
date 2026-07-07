# subscription

**Framework**: StoreKit  
**Kind**: property

The subscription information for an auto-renewable subscripton.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let subscription: Product.SubscriptionInfo?
```

#### Discussion

A `nil` value indicates that this product isn’t an auto-renewable subscription.

For more information about subscriptions, see [`Auto-renewable Subscriptions`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#groups).

## See Also

- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [Product.SubscriptionPeriod](product/subscriptionperiod.md)
  Values that represent the duration of time between subscription renewals.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscription)*