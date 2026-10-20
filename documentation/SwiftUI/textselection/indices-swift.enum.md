# TextSelection.Indices

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [case multiSelection(RangeSet<String.Index>)](./indices-swift.enum/multiselection%28_%29.md)
  The range-set of the selections.
- [TextSelection.Indices.selection(_:)](./indices-swift.enum/selection%28_%29.md)
  The range of the single selection. This may also an represent insertion points if `range.lowerBound == range.upperBound`.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselection/indices-swift.enum)*