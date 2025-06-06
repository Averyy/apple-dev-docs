# formIndex(after:)

**Framework**: TabularData  
**Kind**: method

Replaces the given index with its successor.

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
func formIndex(after i: inout Self.Index)
```

## Parameters

- `i`: A valid index of the collection.   must be less than   .

## See Also

- [var startIndex: Int](rowgrouping/startindex.md)
  The index of the initial group in the row grouping.
- [var endIndex: Int](rowgrouping/endindex.md)
  The index of the final group in the row grouping.
- [func index(before: Int) -> Int](rowgrouping/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](rowgrouping/index(after:).md)
  Returns the index immediately after an element index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](rowgrouping/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(before: inout Self.Index)](rowgrouping/formindex(before:).md)
  Replaces the given index with its predecessor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/formindex(after:))*