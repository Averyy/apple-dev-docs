# SubscriptionOptionGroup

**Framework**: StoreKit  
**Kind**: struct

A group of subscription options that includes optional views for labels and marketing content.

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
@preconcurrency struct SubscriptionOptionGroup<Content, Label, MarketingContent> where Content : StoreContent, Label : View, MarketingContent : View
```

## Topics

### Creating subscription option groups
- [init(LocalizedStringKey, content: () -> Content)](subscriptionoptiongroup/init(_:content:)-2nlpw.md)
- [init(some StringProtocol, content: () -> Content)](subscriptionoptiongroup/init(_:content:)-24grh.md)
- [init(LocalizedStringKey, content: () -> Content, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(_:content:marketingcontent:)-9jybc.md)
- [init(some StringProtocol, content: () -> Content, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(_:content:marketingcontent:)-550q0.md)
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool)](subscriptionoptiongroup/init(_:isincluded:)-uhqa.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool)](subscriptionoptiongroup/init(_:isincluded:)-5f3ml.md)
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(_:isincluded:marketingcontent:)-8vmdm.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(_:isincluded:marketingcontent:)-4d72a.md)
- [init(content: () -> Content)](subscriptionoptiongroup/init(content:).md)
- [init(content: () -> Content, label: () -> Label)](subscriptionoptiongroup/init(content:label:).md)
- [init(content: () -> Content, label: () -> Label, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(content:label:marketingcontent:).md)
- [init(content: () -> Content, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(content:marketingcontent:).md)
- [init(isIncluded: (Product) -> Bool)](subscriptionoptiongroup/init(isincluded:).md)
- [init(isIncluded: (Product) -> Bool, label: () -> Label)](subscriptionoptiongroup/init(isincluded:label:).md)
- [init(isIncluded: (Product) -> Bool, label: () -> Label, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(isincluded:label:marketingcontent:).md)
- [init(isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](subscriptionoptiongroup/init(isincluded:marketingcontent:).md)
### Supporting types
- [struct AutomaticSubscriptionOptionGroupLabel](automaticsubscriptionoptiongrouplabel.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [StoreContent](storecontent.md)

## See Also

- [struct SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [struct SubscriptionOptionSection](subscriptionoptionsection.md)
- [protocol StoreContent](storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroup)*