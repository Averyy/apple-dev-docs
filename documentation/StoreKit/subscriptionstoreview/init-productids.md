# init(productIDs:)

**Framework**: StoreKit  
**Kind**: init

Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.

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
init(productIDs: some Collection<String>) where Content == AutomaticSubscriptionStoreMarketingContent
```

## Parameters

- `productIDs`: The product identifiers to load from the App Store.

## See Also

- [init(groupID: String, visibleRelationships: Product.SubscriptionRelationship)](subscriptionstoreview/init(groupid:visiblerelationships:).md)
  Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.
- [init(subscriptions: some Collection<Product>)](subscriptionstoreview/init(subscriptions:).md)
  Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(productids:))*