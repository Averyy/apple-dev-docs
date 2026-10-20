# updates

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The asynchronous sequence that emits status information when a subscription’s status changes.

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
static var updates: Product.SubscriptionInfo.Status.Statuses { get }
```

## Mentions

- [Managing Price Increases for Auto-Renewable Subscriptions](../../../managing-price-increases-for-auto-renewable-subscriptions.md)

## See Also

### Monitoring subscription status changes
- [static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])>](./all.md)
- [Product.SubscriptionInfo.Status.Statuses](./statuses.md)
  An asynchronous sequence that listens for new subscription status information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/updates)*