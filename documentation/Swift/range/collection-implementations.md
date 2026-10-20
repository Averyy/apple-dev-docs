# Collection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: Range<Bound>.Index](./endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<Bound>.Indices](./indices-swift.property.md)
  The indices that are valid for subscripting the range, in ascending order.
- [var startIndex: Range<Bound>.Index](./startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Range<Bound>.Index, to: Range<Bound>.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func index(Range<Bound>.Index, offsetBy: Int) -> Range<Bound>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(after: Range<Bound>.Index) -> Range<Bound>.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Range<Range<Bound>.Index>) -> Range<Bound>](./subscript%28_%29-358vm.md)
  Accesses the subsequence bounded by the given range.
- [subscript(Range<Bound>.Index) -> Range<Bound>.Element](./subscript%28_%29-84ykx.md)
  Accesses the element at specified position.
### Type Aliases
- [typealias Index](./index.md)
  A type that represents a position in the range.
- [typealias Indices](./indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [typealias SubSequence](./subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/collection-implementations)*