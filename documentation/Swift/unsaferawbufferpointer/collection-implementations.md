# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](unsaferawbufferpointer/count.md)
  The number of bytes in the buffer.
- [var endIndex: UnsafeRawBufferPointer.Index](unsaferawbufferpointer/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](unsaferawbufferpointer/first.md)
  The first element of the collection.
- [var indices: UnsafeRawBufferPointer.Indices](unsaferawbufferpointer/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](unsaferawbufferpointer/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: UnsafeRawBufferPointer.Index](unsaferawbufferpointer/startindex.md)
  Always zero, which is the index of the first byte in a nonempty buffer.
- [var underestimatedCount: Int](unsaferawbufferpointer/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsaferawbufferpointer/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](unsaferawbufferpointer/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](unsaferawbufferpointer/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](unsaferawbufferpointer/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](unsaferawbufferpointer/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](unsaferawbufferpointer/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](unsaferawbufferpointer/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](unsaferawbufferpointer/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](unsaferawbufferpointer/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](unsaferawbufferpointer/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](unsaferawbufferpointer/map(_:)-5p6ph.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](unsaferawbufferpointer/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](unsaferawbufferpointer/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](unsaferawbufferpointer/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsaferawbufferpointer/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](unsaferawbufferpointer/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](unsaferawbufferpointer/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](unsaferawbufferpointer/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](unsaferawbufferpointer/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](unsaferawbufferpointer/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](unsaferawbufferpointer/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](unsaferawbufferpointer/subscript(_:)-2nyad.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](unsaferawbufferpointer/subscript(_:)-392oj.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](unsaferawbufferpointer/subscript(_:)-4al9g.md)
- [subscript(Int) -> UnsafeRawBufferPointer.Element](unsaferawbufferpointer/subscript(_:)-4dk2n.md)
  Accesses the byte at the given offset in the memory region as a `UInt8` value.
- [subscript<R>(R) -> Self.SubSequence](unsaferawbufferpointer/subscript(_:)-4h7s7.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<Int>) -> UnsafeRawBufferPointer.SubSequence](unsaferawbufferpointer/subscript(_:)-58r3z.md)
  Accesses the bytes in the specified memory region.
### Type Aliases
- [UnsafeRawBufferPointer.Index](unsaferawbufferpointer/index.md)
  A type that represents a position in the collection.
- [UnsafeRawBufferPointer.Indices](unsaferawbufferpointer/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [UnsafeRawBufferPointer.SubSequence](unsaferawbufferpointer/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/collection-implementations)*