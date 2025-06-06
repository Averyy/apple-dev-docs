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

- [var startIndex: Int](column/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Int](column/endindex.md)
  The index of the final element in the column.
- [func index(before: Int) -> Int](column/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](column/index(after:).md)
  Returns the index immediately after an element index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](column/index(_:offsetby:limitedby:).md)
- [func formIndex(after: inout Self.Index)](column/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/formindex(before:))*