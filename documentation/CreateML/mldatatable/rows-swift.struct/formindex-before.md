# formIndex(before:)

**Framework**: Create ML  
**Kind**: method

Replaces the given index with its predecessor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func formIndex(before i: inout Self.Index)
```

## Parameters

- `i`: A valid index of the collection.   must be greater than   .

## See Also

- [var startIndex: Int](mldatatable/rows-swift.struct/startindex.md)
  The position of the first row in a nonempty DataTable. If the DataTable is empty, `startIndex` is equal to `endIndex`.
- [var endIndex: Int](mldatatable/rows-swift.struct/endindex.md)
  The DataTable’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func formIndex(after: inout Self.Index)](mldatatable/rows-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(inout Self.Index, offsetBy: Int)](mldatatable/rows-swift.struct/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](mldatatable/rows-swift.struct/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](mldatatable/rows-swift.struct/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/formindex(before:))*