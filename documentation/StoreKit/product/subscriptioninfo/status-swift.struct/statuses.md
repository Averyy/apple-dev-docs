# Product.SubscriptionInfo.Status.Statuses

**Framework**: StoreKit  
**Kind**: struct

An asynchronous sequence that listens for new subscription status information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Statuses
```

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static var updates: Product.SubscriptionInfo.Status.Statuses](product/subscriptioninfo/status-swift.struct/updates.md)
  The asynchronous sequence that emits status information when a subscription’s status changes.
- [static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])>](product/subscriptioninfo/status-swift.struct/all.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/statuses)*