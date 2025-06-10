# SubscriptionOfferView

**Framework**: StoreKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct SubscriptionOfferView<Icon, PlaceholderIcon> where Icon : View, PlaceholderIcon : View
```

## Topics

### Initializers
- [init(SubscriptionOfferViewStyleConfiguration)](subscriptionofferview/init(_:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship)](subscriptionofferview/init(groupid:visiblerelationship:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, icon: () -> Icon)](subscriptionofferview/init(groupid:visiblerelationship:icon:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](subscriptionofferview/init(groupid:visiblerelationship:icon:placeholdericon:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, useAppIcon: Bool)](subscriptionofferview/init(groupid:visiblerelationship:useappicon:).md)
- [init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](subscriptionofferview/init(id:icon:placeholdericon:).md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool)](subscriptionofferview/init(id:preferspromotionalicon:).md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)](subscriptionofferview/init(id:preferspromotionalicon:icon:).md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](subscriptionofferview/init(id:preferspromotionalicon:icon:placeholdericon:).md)
- [init(Product, icon: (ProductIconPhase) -> Icon)](subscriptionofferview/init(_:icon:).md)
- [init(Product, prefersPromotionalIcon: Bool)](subscriptionofferview/init(_:preferspromotionalicon:).md)
- [init(Product, prefersPromotionalIcon: Bool, icon: () -> Icon)](subscriptionofferview/init(_:preferspromotionalicon:icon:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct ProductView](productview.md)
  A view that merchandises an individual In-App Purchase product.
- [struct StoreView](storeview.md)
  A view that merchandises a collection of In-App Purchase products.
- [struct SubscriptionStoreView](subscriptionstoreview.md)
  A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [Backyard Birds: Building an app with SwiftData and widgets](../SwiftUI/Backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionofferview)*