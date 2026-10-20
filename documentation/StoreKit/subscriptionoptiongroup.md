# SubscriptionOptionGroup

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A group of subscription options that includes optional views for labels and marketing content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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
- [init(LocalizedStringKey, content: () -> Content)](./subscriptionoptiongroup/init%28_,content%29-2nlpw.md)
- [init(some StringProtocol, content: () -> Content)](./subscriptionoptiongroup/init%28_,content%29-24grh.md)
- [init(LocalizedStringKey, content: () -> Content, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28_,content,marketingcontent%29-9jybc.md)
- [init(some StringProtocol, content: () -> Content, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28_,content,marketingcontent%29-550q0.md)
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool)](./subscriptionoptiongroup/init%28_,isincluded%29-uhqa.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool)](./subscriptionoptiongroup/init%28_,isincluded%29-5f3ml.md)
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28_,isincluded,marketingcontent%29-8vmdm.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28_,isincluded,marketingcontent%29-4d72a.md)
- [init(content: () -> Content)](./subscriptionoptiongroup/init%28content%29.md)
- [init(content: () -> Content, label: () -> Label)](./subscriptionoptiongroup/init%28content,label%29.md)
- [init(content: () -> Content, label: () -> Label, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28content,label,marketingcontent%29.md)
- [init(content: () -> Content, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28content,marketingcontent%29.md)
- [init(isIncluded: (Product) -> Bool)](./subscriptionoptiongroup/init%28isincluded%29.md)
- [init(isIncluded: (Product) -> Bool, label: () -> Label)](./subscriptionoptiongroup/init%28isincluded,label%29.md)
- [init(isIncluded: (Product) -> Bool, label: () -> Label, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28isincluded,label,marketingcontent%29.md)
- [init(isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](./subscriptionoptiongroup/init%28isincluded,marketingcontent%29.md)
### Supporting types
- [struct AutomaticSubscriptionOptionGroupLabel](./automaticsubscriptionoptiongrouplabel.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [StoreContent](./storecontent.md)

## See Also

### Declaring the structure of a subscription store
- [struct SubscriptionOptionGroupSet](./subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](./subscriptionperiodgroupset.md)
- [struct SubscriptionOptionSection](./subscriptionoptionsection.md)
- [protocol StoreContent](./storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](./storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroup)*