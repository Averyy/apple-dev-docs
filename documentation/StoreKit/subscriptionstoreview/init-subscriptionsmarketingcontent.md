# init(subscriptions:marketingContent:)

**Framework**: StoreKit  
**Kind**: init

Creates a view that displays a collection of subscription options, and merchandises them with custom marketing content.

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
init(subscriptions: some Collection<Product>, @ViewBuilder marketingContent: () -> Content)
```

## Parameters

- `subscriptions`: A collection of auto-renewable subscription   instances to merchandise. The auto-renewable subscriptions need to belong to the same subscription group.
- `marketingContent`: A view that contains marketing content to display above the store controls.

## See Also

- [init(groupID: String, visibleRelationships: Product.SubscriptionRelationship, marketingContent: () -> Content)](subscriptionstoreview/init(groupid:visiblerelationships:marketingcontent:).md)
  Creates a view that loads all the subscriptions in a subscription group from the App Store, and merchandises them with custom marketing content.
- [init(productIDs: some Collection<String>, marketingContent: () -> Content)](subscriptionstoreview/init(productids:marketingcontent:).md)
  Creates a view that loads a collection of subscriptions from the App Store, and merchandises them with custom marketing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(subscriptions:marketingcontent:))*