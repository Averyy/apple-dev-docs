# max()

**Framework**: Tabulardata  
**Kind**: method

Returns the maximum element in the sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@warn_unqualified_access
func max() -> Self.Element?
```

#### Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

#### Discussion

This example finds the largest value in an array of height measurements.

```None
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let greatestHeight = heights.max()
print(greatestHeight)
// Prints "Optional(67.5)"
```

> **Note**: O(), where  is the length of the sequence.

## See Also

- [func min() -> Self.Element?](filledcolumn/min-8lyjh.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](filledcolumn/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](filledcolumn/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](filledcolumn/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/max()-4ilyr)*