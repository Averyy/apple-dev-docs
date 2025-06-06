# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](unsafemutablerawbufferpointer/count.md)
  The number of bytes in the buffer.
- [var endIndex: UnsafeMutableRawBufferPointer.Index](unsafemutablerawbufferpointer/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](unsafemutablerawbufferpointer/first.md)
  The first element of the collection.
- [var indices: UnsafeMutableRawBufferPointer.Indices](unsafemutablerawbufferpointer/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](unsafemutablerawbufferpointer/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: UnsafeMutableRawBufferPointer.Index](unsafemutablerawbufferpointer/startindex.md)
  Always zero, which is the index of the first byte in a nonempty buffer.
- [var underestimatedCount: Int](unsafemutablerawbufferpointer/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsafemutablerawbufferpointer/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](unsafemutablerawbufferpointer/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](unsafemutablerawbufferpointer/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](unsafemutablerawbufferpointer/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](unsafemutablerawbufferpointer/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](unsafemutablerawbufferpointer/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](unsafemutablerawbufferpointer/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](unsafemutablerawbufferpointer/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](unsafemutablerawbufferpointer/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](unsafemutablerawbufferpointer/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](unsafemutablerawbufferpointer/map(_:)-5p6ol.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](unsafemutablerawbufferpointer/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](unsafemutablerawbufferpointer/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](unsafemutablerawbufferpointer/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsafemutablerawbufferpointer/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](unsafemutablerawbufferpointer/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](unsafemutablerawbufferpointer/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](unsafemutablerawbufferpointer/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](unsafemutablerawbufferpointer/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](unsafemutablerawbufferpointer/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](unsafemutablerawbufferpointer/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](unsafemutablerawbufferpointer/subscript(_:)-2nyb9.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](unsafemutablerawbufferpointer/subscript(_:)-392pf.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](unsafemutablerawbufferpointer/subscript(_:)-4al8k.md)
- [subscript<R>(R) -> Self.SubSequence](unsafemutablerawbufferpointer/subscript(_:)-4h7rb.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [UnsafeMutableRawBufferPointer.Index](unsafemutablerawbufferpointer/index.md)
  A type that represents a position in the collection.
- [UnsafeMutableRawBufferPointer.Indices](unsafemutablerawbufferpointer/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [UnsafeMutableRawBufferPointer.SubSequence](unsafemutablerawbufferpointer/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/collection-implementations)*