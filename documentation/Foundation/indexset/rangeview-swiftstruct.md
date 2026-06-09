# IndexSet.RangeView

**Framework**: Foundation  
**Kind**: struct

A view of the contents of an IndexSet, organized by range.

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
struct RangeView
```

#### Overview

For example, if an IndexSet is composed of: `[1..<5]` and `[7..<10]` and `[13]` then calling `next()` on this view’s iterator will produce 3 ranges before returning nil.

## Topics

### Counting Indexes
- [var count: Int](indexset/count.md)
  Returns the number of integers in `self`.
- [let endIndex: IndexSet.RangeView.Index](indexset/rangeview-swift.struct/endindex.md)
  The ending index in the range.
- [var first: IndexSet.Element?](indexset/first.md)
  The first integer in `self`, or nil if `self` is empty.
- [var isEmpty: Bool](indexset/isempty.md)
  Returns `true` if self contains no values.
- [var last: IndexSet.Element?](indexset/last.md)
  The last integer in `self`, or nil if `self` is empty.
- [let startIndex: IndexSet.RangeView.Index](indexset/rangeview-swift.struct/startindex.md)
  The beginning index in the range.
### Accessing Indexes
- [subscript(Range<IndexSet.RangeView.Index>) -> Slice<IndexSet.RangeView>](indexset/rangeview-swift.struct/subscript(_:)-5r66q.md)
  Accesses the items at the given range of indexes.
- [subscript(IndexSet.RangeView.Index) -> Range<IndexSet.Element>](indexset/rangeview-swift.struct/subscript(_:)-8gh0x.md)
  Accesses the item at the given index.
### Finding Indexes
- [let startIndex: IndexSet.RangeView.Index](indexset/rangeview-swift.struct/startindex.md)
  The beginning index in the range.
- [let endIndex: IndexSet.RangeView.Index](indexset/rangeview-swift.struct/endindex.md)
  The ending index in the range.
- [func index(after: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](indexset/rangeview-swift.struct/index(after:).md)
  Returns the index in the range after the specified one.
- [func index(before: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](indexset/rangeview-swift.struct/index(before:).md)
  Returns the index in the range before the specified one.
### Iterating over Indexes
- [func makeIterator() -> IndexingIterator<IndexSet.RangeView>](indexset/rangeview-swift.struct/makeiterator.md)
  Returns an iterator over the indexes of this range view.
### Testing for Inclusion in the Range
- [func contains(IndexSet.Element) -> Bool](indexset/contains(_:).md)
  Returns `true` if `self` contains `integer`.
- [func index(after: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](indexset/rangeview-swift.struct/index(after:).md)
  Returns the index in the range after the specified one.
- [func index(before: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](indexset/rangeview-swift.struct/index(before:).md)
  Returns the index in the range before the specified one.
- [func makeIterator() -> IndexingIterator<IndexSet.RangeView>](indexset/rangeview-swift.struct/makeiterator.md)
  Returns an iterator over the indexes of this range view.
### Type Aliases
- [IndexSet.RangeView.Index](indexset/rangeview-swift.struct/index.md)
  An alias for the type of an index.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func rangeView(of: Range<IndexSet.Element>) -> IndexSet.RangeView](indexset/rangeview(of:)-5xqe8.md)
  Returns a `Range`-based view of `self`.
- [var rangeView: IndexSet.RangeView](indexset/rangeview-swift.property.md)
  Returns a `Range`-based view of the entire contents of `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/rangeview-swift.struct)*