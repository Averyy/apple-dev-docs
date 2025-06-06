# startIndex

**Framework**: TabularData  
**Kind**: property

The index of the initial element in the column slice.

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
var startIndex: Int { get }
```

## See Also

- [var endIndex: Int](columnslice/endindex.md)
  The index of the final element in the column slice.
- [func index(before: Int) -> Int](columnslice/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](columnslice/index(after:).md)
  Returns the index immediately after an element index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](columnslice/index(_:offsetby:limitedby:).md)
- [func formIndex(before: inout Self.Index)](columnslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(after: inout Self.Index)](columnslice/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/startindex)*