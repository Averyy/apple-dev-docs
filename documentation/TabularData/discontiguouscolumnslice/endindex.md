# endIndex

**Framework**: TabularData  
**Kind**: property

The index of the final element in the column slice.

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
var endIndex: Int { get }
```

## See Also

- [var startIndex: Int](discontiguouscolumnslice/startindex.md)
  The index of the initial element in the column slice.
- [func index(before: Int) -> Int](discontiguouscolumnslice/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](discontiguouscolumnslice/index(after:).md)
  Returns the index immediately after an element index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](discontiguouscolumnslice/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](discontiguouscolumnslice/index(_:offsetby:limitedby:).md)
- [func formIndex(before: inout Self.Index)](discontiguouscolumnslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(after: inout Self.Index)](discontiguouscolumnslice/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/endindex)*