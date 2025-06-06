# min()

**Framework**: Foundation  
**Kind**: method

Returns the minimum element in the sequence.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@warn_unqualified_access
func min() -> Self.Element?
```

#### Return Value

The sequence’s minimum element. If the sequence has no elements, returns `nil`.

#### Discussion

This example finds the smallest value in an array of height measurements.

```None
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let lowestHeight = heights.min()
print(lowestHeight)
// Prints "Optional(58.5)"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## See Also

- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](data/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func max() -> Self.Element?](data/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](data/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](data/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func range(of: Data, options: Data.SearchOptions, in: Range<Data.Index>?) -> Range<Data.Index>?](data/range(of:options:in:).md)
  Finds the range of the specified data as a subsequence of this data, if it exists.
- [typealias SearchOptions](data/searchoptions.md)
  Options that control a data search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/min())*