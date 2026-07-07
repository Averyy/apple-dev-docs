# init(idType:groupedBy:label:marketingContent:)

**Framework**: StoreKit  
**Kind**: init

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
@preconcurrency init(idType: GroupID.Type = GroupID.self, groupedBy transform: @escaping (Product) -> GroupID, @ViewBuilder label: @escaping (GroupID) -> Label, @ViewBuilder marketingContent: @escaping (GroupID) -> MarketingContent)
```

## See Also

- [init(idType: GroupID.Type, groupedBy: (Product) -> GroupID, label: (GroupID) -> Label)](subscriptionoptiongroupset/init(idtype:groupedby:label:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroupset/init(idtype:groupedby:label:marketingcontent:))*