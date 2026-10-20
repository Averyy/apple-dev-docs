# IndexSet.RangeView

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [var count: Int](./count.md)
  Returns the number of integers in `self`.
- [let endIndex: IndexSet.RangeView.Index](./rangeview-swift.struct/endindex.md)
  The ending index in the range.
- [var first: IndexSet.Element?](./first.md)
  The first integer in `self`, or nil if `self` is empty.
- [var isEmpty: Bool](./isempty.md)
  Returns `true` if self contains no values.
- [var last: IndexSet.Element?](./last.md)
  The last integer in `self`, or nil if `self` is empty.
- [let startIndex: IndexSet.RangeView.Index](./rangeview-swift.struct/startindex.md)
  The beginning index in the range.
### Accessing Indexes
- [subscript(Range<IndexSet.RangeView.Index>) -> Slice<IndexSet.RangeView>](./rangeview-swift.struct/subscript%28_%29-5r66q.md)
  Accesses the items at the given range of indexes.
- [subscript(IndexSet.RangeView.Index) -> Range<IndexSet.Element>](./rangeview-swift.struct/subscript%28_%29-8gh0x.md)
  Accesses the item at the given index.
### Finding Indexes
- [let startIndex: IndexSet.RangeView.Index](./rangeview-swift.struct/startindex.md)
  The beginning index in the range.
- [let endIndex: IndexSet.RangeView.Index](./rangeview-swift.struct/endindex.md)
  The ending index in the range.
- [func index(after: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](./rangeview-swift.struct/index%28after%29.md)
  Returns the index in the range after the specified one.
- [func index(before: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](./rangeview-swift.struct/index%28before%29.md)
  Returns the index in the range before the specified one.
### Iterating over Indexes
- [func makeIterator() -> IndexingIterator<IndexSet.RangeView>](./rangeview-swift.struct/makeiterator%28%29.md)
  Returns an iterator over the indexes of this range view.
### Testing for Inclusion in the Range
- [func contains(IndexSet.Element) -> Bool](./contains%28_%29.md)
  Returns `true` if `self` contains `integer`.
- [func index(after: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](./rangeview-swift.struct/index%28after%29.md)
  Returns the index in the range after the specified one.
- [func index(before: IndexSet.RangeView.Index) -> IndexSet.RangeView.Index](./rangeview-swift.struct/index%28before%29.md)
  Returns the index in the range before the specified one.
- [func makeIterator() -> IndexingIterator<IndexSet.RangeView>](./rangeview-swift.struct/makeiterator%28%29.md)
  Returns an iterator over the indexes of this range view.
### Type Aliases
- [IndexSet.RangeView.Index](./rangeview-swift.struct/index.md)
  An alias for the type of an index.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Getting a Range-Based View
- [func rangeView(of: Range<IndexSet.Element>) -> IndexSet.RangeView](./rangeview%28of%29-5xqe8.md)
  Returns a `Range`-based view of `self`.
- [var rangeView: IndexSet.RangeView](./rangeview-swift.property.md)
  Returns a `Range`-based view of the entire contents of `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/rangeview-swift.struct)*