# SubscriptionOfferView

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SubscriptionOfferView<Icon, PlaceholderIcon> where Icon : View, PlaceholderIcon : View
```

## Topics

### Initializers
- [init(SubscriptionOfferViewStyleConfiguration)](./subscriptionofferview/init%28_%29.md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship)](./subscriptionofferview/init%28groupid,visiblerelationship%29.md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, icon: () -> Icon)](./subscriptionofferview/init%28groupid,visiblerelationship,icon%29.md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](./subscriptionofferview/init%28groupid,visiblerelationship,icon,placeholdericon%29.md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, useAppIcon: Bool)](./subscriptionofferview/init%28groupid,visiblerelationship,useappicon%29.md)
- [init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](./subscriptionofferview/init%28id,icon,placeholdericon%29.md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool)](./subscriptionofferview/init%28id,preferspromotionalicon%29.md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon)](./subscriptionofferview/init%28id,preferspromotionalicon,icon%29.md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](./subscriptionofferview/init%28id,preferspromotionalicon,icon,placeholdericon%29.md)
- [init(Product, icon: (ProductIconPhase) -> Icon)](./subscriptionofferview/init%28_,icon%29.md)
- [init(Product, prefersPromotionalIcon: Bool)](./subscriptionofferview/init%28_,preferspromotionalicon%29.md)
- [init(Product, prefersPromotionalIcon: Bool, icon: () -> Icon)](./subscriptionofferview/init%28_,preferspromotionalicon,icon%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Merchandising Apple In-App Purchases, subscriptions, and offers
- [struct ProductView](./productview.md)
  A view that merchandises an individual Apple In-App Purchase product.
- [struct StoreView](./storeview.md)
  A view that merchandises a collection of Apple In-App Purchase products.
- [struct SubscriptionStoreView](./subscriptionstoreview.md)
  A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [Backyard Birds: Building an app with SwiftData and widgets](../SwiftUI/backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionofferview)*