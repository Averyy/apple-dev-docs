# index(_:offsetBy:limitedBy:)

**Framework**: TabularData  
**Kind**: method

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
func index(_ i: Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Self.Index?
```

## See Also

- [var startIndex: Int](column/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Int](column/endindex.md)
  The index of the final element in the column.
- [func index(before: Int) -> Int](column/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](column/index(after:).md)
  Returns the index immediately after an element index.
- [func formIndex(before: inout Self.Index)](column/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(after: inout Self.Index)](column/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/index(_:offsetby:limitedby:))*