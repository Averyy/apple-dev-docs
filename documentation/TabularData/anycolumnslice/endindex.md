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

- [var startIndex: Int](anycolumnslice/startindex.md)
  The index of the initial element in the column slice.
- [func index(before: Int) -> Int](anycolumnslice/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](anycolumnslice/index(after:).md)
  Returns the index immediately after an element index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](anycolumnslice/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(before: inout Self.Index)](anycolumnslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(after: inout Self.Index)](anycolumnslice/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/endindex)*