# bundleSubscriptionGroupID

**Framework**: StoreKit  
**Kind**: property

Identifies the subscription bundle group the next renewal is for.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var bundleSubscriptionGroupID: String? { get }
```

#### Discussion

> **Note**: Only for renewals of subscriptions included in a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/bundlesubscriptiongroupid)*