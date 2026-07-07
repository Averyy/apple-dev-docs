# init(productIDs:marketingContent:)

**Framework**: StoreKit  
**Kind**: init

Creates a view that loads a collection of subscriptions from the App Store, and merchandises them with custom marketing content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(productIDs: some Collection<String>, @ViewBuilder marketingContent: () -> Content)
```

## Parameters

- `productIDs`: The product identifiers to load from the App Store.
- `marketingContent`: The view that contains marketing content to display above the store controls.

## See Also

- [init(groupID: String, visibleRelationships: Product.SubscriptionRelationship, marketingContent: () -> Content)](subscriptionstoreview/init(groupid:visiblerelationships:marketingcontent:).md)
  Creates a view that loads all the subscriptions in a subscription group from the App Store, and merchandises them with custom marketing content.
- [init(subscriptions: some Collection<Product>, marketingContent: () -> Content)](subscriptionstoreview/init(subscriptions:marketingcontent:).md)
  Creates a view that displays a collection of subscription options, and merchandises them with custom marketing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(productids:marketingcontent:))*