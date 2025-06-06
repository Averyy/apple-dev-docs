# init(groupID:visibleRelationships:marketingContent:)

**Framework**: StoreKit  
**Kind**: init

Creates a view that loads all the subscriptions in a subscription group from the App Store, and merchandises them with custom marketing content.

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
init(groupID: String, visibleRelationships: Product.SubscriptionRelationship = .all, @ViewBuilder marketingContent: () -> Content)
```

## Parameters

- `groupID`: The subscription group identifier to load from the App Store.
- `visibleRelationships`: The kinds of subscription option relationships the view makes visible when someone is already subscribed to the subscription.
- `marketingContent`: The view that contains marketing content to display above the store controls.

## See Also

- [init(productIDs: some Collection<String>, marketingContent: () -> Content)](subscriptionstoreview/init(productids:marketingcontent:).md)
  Creates a view that loads a collection of subscriptions from the App Store, and merchandises them with custom marketing content.
- [init(subscriptions: some Collection<Product>, marketingContent: () -> Content)](subscriptionstoreview/init(subscriptions:marketingcontent:).md)
  Creates a view that displays a collection of subscription options, and merchandises them with custom marketing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:marketingcontent:))*