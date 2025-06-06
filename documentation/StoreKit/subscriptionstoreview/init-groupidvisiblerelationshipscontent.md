# init(groupID:visibleRelationships:content:)

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
init<C>(groupID: String, visibleRelationships: Product.SubscriptionRelationship = .all, @StoreContentBuilder content: () -> C) where Content == SubscriptionStoreContentView<C>, C : StoreContent
```

## See Also

- [init<C>(productIDs: some Collection<String>, content: () -> C)](subscriptionstoreview/init(productids:content:).md)
- [init<C>(subscriptions: some Collection<Product>, content: () -> C)](subscriptionstoreview/init(subscriptions:content:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:content:))*