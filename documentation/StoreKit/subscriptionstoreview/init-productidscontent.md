# init(productIDs:content:)

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
init<C>(productIDs: some Collection<String>, @StoreContentBuilder content: () -> C) where Content == SubscriptionStoreContentView<C>, C : StoreContent
```

## See Also

- [init<C>(groupID: String, visibleRelationships: Product.SubscriptionRelationship, content: () -> C)](subscriptionstoreview/init(groupid:visiblerelationships:content:).md)
- [init<C>(subscriptions: some Collection<Product>, content: () -> C)](subscriptionstoreview/init(subscriptions:content:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(productids:content:))*