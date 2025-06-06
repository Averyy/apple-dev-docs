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

- [var startIndex: Int](anycolumn/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Int](anycolumn/endindex.md)
  The index of the final element in the column.
- [func index(before: Int) -> Int](anycolumn/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](anycolumn/index(after:).md)
  Returns the index immediately after an element index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](anycolumn/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(after: inout Self.Index)](anycolumn/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/formindex(before:))*