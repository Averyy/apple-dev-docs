# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: ClosedRange<Bound>.Index](closedrange/endindex.md)
  The range’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](closedrange/isempty.md)
  A Boolean value indicating whether the range contains no elements.
- [var startIndex: ClosedRange<Bound>.Index](closedrange/startindex.md)
  The position of the first element in the range.
### Instance Methods
- [func distance(from: ClosedRange<Bound>.Index, to: ClosedRange<Bound>.Index) -> Int](closedrange/distance(from:to:).md)
  Returns the distance between two indices.
- [func index(ClosedRange<Bound>.Index, offsetBy: Int) -> ClosedRange<Bound>.Index](closedrange/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(after: ClosedRange<Bound>.Index) -> ClosedRange<Bound>.Index](closedrange/index(after:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(ClosedRange<Bound>.Index) -> Bound](closedrange/subscript(_:)-60m0l.md)
  Accesses the element at specified position.
- [subscript(Range<ClosedRange<Bound>.Index>) -> Slice<ClosedRange<Bound>>](closedrange/subscript(_:)-vph6.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [ClosedRange.Indices](closedrange/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [ClosedRange.SubSequence](closedrange/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Enumerations
- [ClosedRange.Index](closedrange/index.md)
  A type that represents a position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/collection-implementations)*