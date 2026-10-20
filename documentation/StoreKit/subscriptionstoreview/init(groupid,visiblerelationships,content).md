# init(groupID:visibleRelationships:content:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init<C>(groupID: String, visibleRelationships: Product.SubscriptionRelationship = .all, @StoreContentBuilder content: () -> C) where Content == SubscriptionStoreContentView<C>, C : StoreContent
```

Available when `Content` conforms to `View`.

## See Also

### Creating subscription store views with a hierarchichal structure
- [init<C>(productIDs: some Collection<String>, content: () -> C)](./init%28productids,content%29.md)
- [init<C>(subscriptions: some Collection<Product>, content: () -> C)](./init%28subscriptions,content%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:content:))*