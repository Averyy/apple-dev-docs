# Product.SubscriptionInfo.Status.Statuses

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that listens for new subscription status information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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
- [AsyncSequence](../../../../Swift/asyncsequence.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Monitoring subscription status changes
- [static var updates: Product.SubscriptionInfo.Status.Statuses](./updates.md)
  The asynchronous sequence that emits status information when a subscription’s status changes.
- [static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])>](./all.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/statuses)*