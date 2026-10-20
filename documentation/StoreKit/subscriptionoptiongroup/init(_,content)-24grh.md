# init(_:content:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

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
@preconcurrency init(_ label: some StringProtocol, @StoreContentBuilder content: () -> Content)
```

Available when `Content` conforms to `StoreContent`, `Label` is `Text`, and `MarketingContent` is `AutomaticSubscriptionStoreMarketingContent`.

## See Also

### Creating subscription option groups
- [init(LocalizedStringKey, content: () -> Content)](./init%28_,content%29-2nlpw.md)
- [init(LocalizedStringKey, content: () -> Content, marketingContent: () -> MarketingContent)](./init%28_,content,marketingcontent%29-9jybc.md)
- [init(some StringProtocol, content: () -> Content, marketingContent: () -> MarketingContent)](./init%28_,content,marketingcontent%29-550q0.md)
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool)](./init%28_,isincluded%29-uhqa.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool)](./init%28_,isincluded%29-5f3ml.md)
- [init(LocalizedStringKey, isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](./init%28_,isincluded,marketingcontent%29-8vmdm.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](./init%28_,isincluded,marketingcontent%29-4d72a.md)
- [init(content: () -> Content)](./init%28content%29.md)
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
- [init(content: () -> Content, label: () -> Label, marketingContent: () -> MarketingContent)](./init%28content,label,marketingcontent%29.md)
- [init(content: () -> Content, marketingContent: () -> MarketingContent)](./init%28content,marketingcontent%29.md)
- [init(isIncluded: (Product) -> Bool)](./init%28isincluded%29.md)
- [init(isIncluded: (Product) -> Bool, label: () -> Label)](./init%28isincluded,label%29.md)
- [init(isIncluded: (Product) -> Bool, label: () -> Label, marketingContent: () -> MarketingContent)](./init%28isincluded,label,marketingcontent%29.md)
- [init(isIncluded: (Product) -> Bool, marketingContent: () -> MarketingContent)](./init%28isincluded,marketingcontent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroup/init(_:content:)-24grh)*