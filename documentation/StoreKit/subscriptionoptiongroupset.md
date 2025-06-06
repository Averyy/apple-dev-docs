# SubscriptionOptionGroupSet

**Framework**: StoreKit  
**Kind**: struct

A set of groups of subscription options that include optional views for labels and marketing content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SubscriptionOptionGroupSet<GroupID, Label, MarketingContent> where GroupID : Hashable, Label : View, MarketingContent : View
```

## Topics

### Creating subscription option group sets
- [init(idType: GroupID.Type, groupedBy: (Product) -> GroupID, label: (GroupID) -> Label)](subscriptionoptiongroupset/init(idtype:groupedby:label:).md)
- [init(idType: GroupID.Type, groupedBy: (Product) -> GroupID, label: (GroupID) -> Label, marketingContent: (GroupID) -> MarketingContent)](subscriptionoptiongroupset/init(idtype:groupedby:label:marketingcontent:).md)
### Creating the group style
- [nonisolated func subscriptionStoreOptionGroupStyle(_ style: some SubscriptionOptionGroupStyle) -> some View
](../SwiftUI/View/subscriptionStoreOptionGroupStyle(_:).md)
  Sets the style subscription store views within this view use to display groups of subscription options.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [StoreContent](storecontent.md)

## See Also

- [struct SubscriptionOptionGroup](subscriptionoptiongroup.md)
  A group of subscription options that includes optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [struct SubscriptionOptionSection](subscriptionoptionsection.md)
- [protocol StoreContent](storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroupset)*