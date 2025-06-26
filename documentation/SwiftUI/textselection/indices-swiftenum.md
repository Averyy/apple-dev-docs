# TextSelection.Indices

**Framework**: SwiftUI  
**Kind**: enum

The indices of the current selection.

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
enum Indices
```

## Topics

### Enumeration Cases
- [case multiSelection(RangeSet<String.Index>)](textselection/indices-swift.enum/multiselection(_:).md)
  The range-set of the selections.
- [TextSelection.Indices.selection(_:)](textselection/indices-swift.enum/selection(_:).md)
  The range of the single selection. This may also an represent insertion points if `range.lowerBound == range.upperBound`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselection/indices-swift.enum)*