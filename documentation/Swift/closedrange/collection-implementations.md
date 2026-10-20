# Collection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: ClosedRange<Bound>.Index](./endindex.md)
  The range’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value indicating whether the range contains no elements.
- [var startIndex: ClosedRange<Bound>.Index](./startindex.md)
  The position of the first element in the range.
### Instance Methods
- [func distance(from: ClosedRange<Bound>.Index, to: ClosedRange<Bound>.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func index(ClosedRange<Bound>.Index, offsetBy: Int) -> ClosedRange<Bound>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(after: ClosedRange<Bound>.Index) -> ClosedRange<Bound>.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(ClosedRange<Bound>.Index) -> Bound](./subscript%28_%29-60m0l.md)
  Accesses the element at specified position.
- [subscript(Range<ClosedRange<Bound>.Index>) -> Slice<ClosedRange<Bound>>](./subscript%28_%29-vph6.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [ClosedRange.Indices](./indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [ClosedRange.SubSequence](./subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Enumerations
- [ClosedRange.Index](./index.md)
  A type that represents a position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/collection-implementations)*