# status

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An array that contains status information for a subscription group, including renewal and transaction information.

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
var status: [Product.SubscriptionInfo.Status] { get async throws }
```

## Discussion

This array is empty if the customer was never subscribed to a product in this subscription group.

The array can have more than one subscription status if your subscription supports Family Sharing. Provide the customer with service for the subscription based on the highest level of service where the state is [`subscribed`](./renewalstate/subscribed.md).

## See Also

### Determining the subscription status
- [static func status(for: String) async throws -> [Product.SubscriptionInfo.Status]](./status%28for%29.md)
  Gets the subscription status for a subscription group identifier.
- [static func status(transactionID: UInt64) async throws -> SubscriptionStatus?](./status%28transactionid%29.md)
  Gets the subscription status for a transaction ID.
- [Product.SubscriptionInfo.Status](./status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.property)*