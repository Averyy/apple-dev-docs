# init(groupID:visibleRelationships:)

**Framework**: StoreKit  
**Kind**: init

Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.

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
init(groupID: String, visibleRelationships: Product.SubscriptionRelationship = .all) where Content == AutomaticSubscriptionStoreMarketingContent
```

## Parameters

- `groupID`: The subscription group identifier to load from the App Store.
- `visibleRelationships`: The kinds of subscription option relationships the view makes visible when someone is already subscribed to the subscription.

## See Also

- [init(productIDs: some Collection<String>)](subscriptionstoreview/init(productids:).md)
  Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.
- [init(subscriptions: some Collection<Product>)](subscriptionstoreview/init(subscriptions:).md)
  Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(groupid:visiblerelationships:))*