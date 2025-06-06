# index(after:)

**Framework**: TabularData  
**Kind**: method

Returns the row index immediately after a row index.

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
func index(after i: Int) -> Int
```

## Parameters

- `i`: A valid index to a row in the collection.

## See Also

- [var startIndex: Int](dataframe/rows-swift.struct/startindex.md)
  The index of the initial row in the collection.
- [var endIndex: Int](dataframe/rows-swift.struct/endindex.md)
  The index of the final row in the collection.
- [func index(before: Int) -> Int](dataframe/rows-swift.struct/index(before:).md)
  Returns the row index immediately before a row index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](dataframe/rows-swift.struct/index(_:offsetby:limitedby:).md)
- [func formIndex(before: inout Self.Index)](dataframe/rows-swift.struct/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(after: inout Self.Index)](dataframe/rows-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/index(after:))*