# formIndex(before:)

**Framework**: TabularData  
**Kind**: method

Replaces the given index with its predecessor.

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
func formIndex(before i: inout Self.Index)
```

## Parameters

- `i`: A valid index of the collection.   must be greater than   .

## See Also

- [var startIndex: Base.Index](filledcolumn/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Base.Index](filledcolumn/endindex.md)
  The index of the final element in the column.
- [func index(before: Base.Index) -> Base.Index](filledcolumn/index(before:).md)
  Returns the row index immediately before a row index.
- [func index(after: Base.Index) -> Base.Index](filledcolumn/index(after:).md)
  Returns the position immediately after an index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](filledcolumn/index(_:offsetby:limitedby:).md)
- [func formIndex(after: inout Self.Index)](filledcolumn/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/formindex(before:))*