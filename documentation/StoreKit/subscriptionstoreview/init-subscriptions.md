# init(subscriptions:)

**Framework**: StoreKit  
**Kind**: init

Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.

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
init(subscriptions: some Collection<Product>) where Content == AutomaticSubscriptionStoreMarketingContent
```

## Parameters

- `subscriptions`: A collection of auto-renewable subscription   instances to merchandise. The auto-renewable subscriptions need to belong to the same subscription group.

## See Also

- [init(groupID: String, visibleRelationships: Product.SubscriptionRelationship)](subscriptionstoreview/init(groupid:visiblerelationships:).md)
  Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.
- [init(productIDs: some Collection<String>)](subscriptionstoreview/init(productids:).md)
  Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstoreview/init(subscriptions:))*