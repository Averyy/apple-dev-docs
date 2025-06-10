# init(id:prefersPromotionalIcon:icon:)

**Framework**: StoreKit  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init(id subscriptionID: Product.ID, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: () -> Icon) where PlaceholderIcon == AutomaticProductPlaceholderIcon
```

## See Also

- [init(SubscriptionOfferViewStyleConfiguration)](subscriptionofferview/init(_:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship)](subscriptionofferview/init(groupid:visiblerelationship:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, icon: () -> Icon)](subscriptionofferview/init(groupid:visiblerelationship:icon:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](subscriptionofferview/init(groupid:visiblerelationship:icon:placeholdericon:).md)
- [init(groupID: String, visibleRelationship: Product.SubscriptionRelationship, useAppIcon: Bool)](subscriptionofferview/init(groupid:visiblerelationship:useappicon:).md)
- [init(id: Product.ID, icon: (ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](subscriptionofferview/init(id:icon:placeholdericon:).md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool)](subscriptionofferview/init(id:preferspromotionalicon:).md)
- [init(id: Product.ID, prefersPromotionalIcon: Bool, icon: () -> Icon, placeholderIcon: () -> PlaceholderIcon)](subscriptionofferview/init(id:preferspromotionalicon:icon:placeholdericon:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionofferview/init(id:preferspromotionalicon:icon:))*