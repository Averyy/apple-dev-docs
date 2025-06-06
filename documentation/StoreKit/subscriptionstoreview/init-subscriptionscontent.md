# init(subscriptions:content:)

**Framework**: StoreKit  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init<C>(subscriptions: some Collection<Product>, @StoreContentBuilder content: () -> C) where Content == SubscriptionStoreContentView<C>, C : StoreContent
```

## See Also

- [init<C>(groupID: String, visibleRelationships: Product.SubscriptionRelationship, content: () -> C)](subscriptionstoreview/init(groupid:visiblerelationships:content:).md)
- [init<C>(productIDs: some Collection<String>, content: () -> C)](subscriptionstoreview/init(productids:content:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(subscriptions:content:))*