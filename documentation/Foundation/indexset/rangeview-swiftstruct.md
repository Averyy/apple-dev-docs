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
- [var first: IndexSet.Element?](indexset/first.md)
  The first integer in `self`, or nil if `self` is empty.
- [var isEmpty: Bool](indexset/isempty.md)
- [var last: IndexSet.Element?](indexset/last.md)
  The last integer in `self`, or nil if `self` is empty.
### Testing for Inclusion in the Range
- [func contains(IndexSet.Element) -> Bool](indexset/contains(_:).md)
  Returns `true` if `self` contains `integer`.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func rangeView(of: Range<IndexSet.Element>) -> IndexSet.RangeView](indexset/rangeview(of:)-5xqe8.md)
  Returns a `Range`-based view of `self`.
- [var rangeView: IndexSet.RangeView](indexset/rangeview-swift.property.md)
  Returns a `Range`-based view of the entire contents of `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/rangeview-swift.struct)*