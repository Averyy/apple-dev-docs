# status(transactionID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Gets the subscription status for a transaction ID.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
static func status(transactionID: UInt64) async throws -> SubscriptionStatus?
```

## See Also

### Determining the subscription status
- [var status: [Product.SubscriptionInfo.Status]](./status-swift.property.md)
  An array that contains status information for a subscription group, including renewal and transaction information.
- [static func status(for: String) async throws -> [Product.SubscriptionInfo.Status]](./status%28for%29.md)
  Gets the subscription status for a subscription group identifier.
- [Product.SubscriptionInfo.Status](./status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status(transactionid:))*