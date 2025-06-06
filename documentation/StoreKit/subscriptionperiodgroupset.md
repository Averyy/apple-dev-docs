# SubscriptionPeriodGroupSet

**Framework**: StoreKit  
**Kind**: struct

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
@preconcurrency struct SubscriptionPeriodGroupSet<Label, MarketingContent> where Label : View, MarketingContent : View
```

## Topics

### Creating subscription period group sets
- [init()](subscriptionperiodgroupset/init.md)
- [init(marketingContent: (Product.SubscriptionPeriod?) -> MarketingContent)](subscriptionperiodgroupset/init(marketingcontent:).md)
- [init(marketingContent: (Product.SubscriptionPeriod?) -> MarketingContent, label: (Product.SubscriptionPeriod?) -> Label)](subscriptionperiodgroupset/init(marketingcontent:label:).md)
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
- [struct SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionOptionSection](subscriptionoptionsection.md)
- [protocol StoreContent](storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionperiodgroupset)*