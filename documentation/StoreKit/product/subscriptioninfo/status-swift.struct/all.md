# all

**Framework**: StoreKit  
**Kind**: property

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])> { get }
```

## See Also

- [static var updates: Product.SubscriptionInfo.Status.Statuses](product/subscriptioninfo/status-swift.struct/updates.md)
  The asynchronous sequence that emits status information when a subscription’s status changes.
- [Product.SubscriptionInfo.Status.Statuses](product/subscriptioninfo/status-swift.struct/statuses.md)
  An asynchronous sequence that listens for new subscription status information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/all)*