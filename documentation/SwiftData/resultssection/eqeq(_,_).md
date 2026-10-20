# ==(_:_:)

**Framework**: SwiftData  
**Kind**: op  
**Role**: Operator

Two sections are equal if they have the same [`title`](./title.md) and contain the same elements, in the same order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func == (lhs: ResultsSection<Element, SectionTitle>, rhs: ResultsSection<Element, SectionTitle>) -> Bool
```

Available when `Element` conforms to `PersistentModel` and `SectionTitle` conforms to `Hashable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssection/==(_:_:))*