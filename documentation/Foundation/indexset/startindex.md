# startIndex

**Framework**: Foundation  
**Kind**: property

The beginning index in the set.

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
var startIndex: IndexSet.Index { get }
```

## See Also

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
- [func indexRange(in: Range<IndexSet.Element>) -> Range<IndexSet.Index>](indexset/indexrange(in:)-539lz.md)
  Return a `Range<IndexSet.Index>` which can be used to subscript the index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/startindex)*