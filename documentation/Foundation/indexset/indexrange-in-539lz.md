# indexRange(in:)

**Framework**: Foundation  
**Kind**: method

Return a `Range<IndexSet.Index>` which can be used to subscript the index set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func indexRange(in range: Range<IndexSet.Element>) -> Range<IndexSet.Index>
```

#### Discussion

The resulting range is the range of the intersection of the integers in `range` with the index set. The resulting range will be `isEmpty` if the intersection is empty.

## Parameters

- `range`: The range of integers to include.

## See Also

- [var startIndex: IndexSet.Index](indexset/startindex.md)
  The beginning index in the set.
- [var endIndex: IndexSet.Index](indexset/endindex.md)
  The ending index in the set.
- [func index(after: IndexSet.Index) -> IndexSet.Index](indexset/index(after:).md)
  Returns the index that follows the given index in the set.
- [func index(before: IndexSet.Index) -> IndexSet.Index](indexset/index(before:).md)
  Returns the index that precedes the given index in the set.
- [func formIndex(after: inout IndexSet.Index)](indexset/formindex(after:).md)
  Modifies the given index to refer to the item after the one it currently refers to.
- [func formIndex(before: inout IndexSet.Index)](indexset/formindex(before:).md)
  Modifies the given index to refer to the item before the one it currently refers to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/indexrange(in:)-539lz)*