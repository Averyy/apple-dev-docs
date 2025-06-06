# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Range<Bound>.Index](range/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<Bound>.Indices](range/indices-swift.property.md)
  The indices that are valid for subscripting the range, in ascending order.
- [var startIndex: Range<Bound>.Index](range/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Range<Bound>.Index, to: Range<Bound>.Index) -> Int](range/distance(from:to:).md)
  Returns the distance between two indices.
- [func index(Range<Bound>.Index, offsetBy: Int) -> Range<Bound>.Index](range/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(after: Range<Bound>.Index) -> Range<Bound>.Index](range/index(after:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Range<Range<Bound>.Index>) -> Range<Bound>](range/subscript(_:)-358vm.md)
  Accesses the subsequence bounded by the given range.
- [subscript(Range<Bound>.Index) -> Range<Bound>.Element](range/subscript(_:)-84ykx.md)
  Accesses the element at specified position.
### Type Aliases
- [typealias Index](range/index.md)
  A type that represents a position in the range.
- [typealias Indices](range/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [typealias SubSequence](range/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/collection-implementations)*