# ==(_:_:)

**Framework**: SwiftData  
**Kind**: op  
**Role**: Operator

Two `SectionedResults` are equal if they contain the same [`ResultsSection`](../resultssection.md) values, in the same order.

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
static func == (lhs: SectionedResults<Element, SectionTitle>, rhs: SectionedResults<Element, SectionTitle>) -> Bool
```

Available when `Element` conforms to `PersistentModel` and `SectionTitle` conforms to `Hashable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/sectionedresults/==(_:_:))*