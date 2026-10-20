# init(idType:groupedBy:label:)

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
@preconcurrency init(idType: GroupID.Type = GroupID.self, groupedBy transform: @escaping (Product) -> GroupID, @ViewBuilder label: @escaping (GroupID) -> Label) where MarketingContent == AutomaticSubscriptionStoreMarketingContent
```

## See Also

### Creating subscription option group sets
- [init(idType: GroupID.Type, groupedBy: (Product) -> GroupID, label: (GroupID) -> Label, marketingContent: (GroupID) -> MarketingContent)](./init%28idtype,groupedby,label,marketingcontent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroupset/init(idtype:groupedby:label:))*