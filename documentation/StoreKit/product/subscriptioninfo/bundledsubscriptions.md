# bundledSubscriptions

**Framework**: StoreKit  
**Kind**: property

Properties and functionality specific to auto-renewable subscriptions included in a subscription bundle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let bundledSubscriptions: [Product.SubscriptionInfo.BundledSubscription]
```

#### Discussion

This list is only populated if `type` is `.subscriptionBundle`, and always empty for all other product types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/bundledsubscriptions)*