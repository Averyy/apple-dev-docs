# SubscriptionOptionSection

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
@preconcurrency struct SubscriptionOptionSection<Header, Content, Footer> where Header : View, Content : StoreContent, Footer : View
```

## Topics

### Creating subscription option sections
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool, footer: () -> Footer)](subscriptionoptionsection/init(_:isincluded:footer:)-17lo3.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool, footer: () -> Footer)](subscriptionoptionsection/init(_:isincluded:footer:)-36k79.md)
- [init(isIncluded: (Product) -> Bool, header: () -> Header, footer: () -> Footer)](subscriptionoptionsection/init(isincluded:header:footer:).md)
### Choosing a subscription option group style
- [nonisolated func subscriptionStoreOptionGroupStyle(_ style: some SubscriptionOptionGroupStyle) -> some View
](../SwiftUI/View/subscriptionStoreOptionGroupStyle(_:).md)
  Sets the style subscription store views within this view use to display groups of subscription options.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StoreContent](storecontent.md)

## See Also

- [struct SubscriptionOptionGroup](subscriptionoptiongroup.md)
  A group of subscription options that includes optional views for labels and marketing content.
- [struct SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [protocol StoreContent](storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptionsection)*