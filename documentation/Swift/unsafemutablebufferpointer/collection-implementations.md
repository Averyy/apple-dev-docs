# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Int](unsafemutablebufferpointer/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](unsafemutablebufferpointer/first.md)
  The first element of the collection.
- [var indices: Range<Int>](unsafemutablebufferpointer/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](unsafemutablebufferpointer/isempty.md)
  A Boolean value indicating whether the buffer is empty.
- [var startIndex: Int](unsafemutablebufferpointer/startindex.md)
  The index of the first element in a nonempty buffer.
- [var underestimatedCount: Int](unsafemutablebufferpointer/underestimatedcount-4ggr6.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Int, to: Int) -> Int](unsafemutablebufferpointer/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsafemutablebufferpointer/drop(while:)-37wq1.md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](unsafemutablebufferpointer/dropfirst(_:)-1ruqu.md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](unsafemutablebufferpointer/droplast(_:)-6rw2x.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](unsafemutablebufferpointer/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](unsafemutablebufferpointer/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](unsafemutablebufferpointer/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](unsafemutablebufferpointer/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Int)](unsafemutablebufferpointer/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Int, offsetBy: Int) -> Int](unsafemutablebufferpointer/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](unsafemutablebufferpointer/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](unsafemutablebufferpointer/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](unsafemutablebufferpointer/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](unsafemutablebufferpointer/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](unsafemutablebufferpointer/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](unsafemutablebufferpointer/map(_:)-5p6og.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](unsafemutablebufferpointer/prefix(_:)-1n69c.md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](unsafemutablebufferpointer/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](unsafemutablebufferpointer/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsafemutablebufferpointer/prefix(while:)-3arjm.md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](unsafemutablebufferpointer/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](unsafemutablebufferpointer/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](unsafemutablebufferpointer/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](unsafemutablebufferpointer/split(maxsplits:omittingemptysubsequences:whereseparator:)-4pbql.md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](unsafemutablebufferpointer/split(separator:maxsplits:omittingemptysubsequences:)-3dgmc.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](unsafemutablebufferpointer/suffix(_:)-qdce.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](unsafemutablebufferpointer/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<Int>) -> Slice<UnsafeMutableBufferPointer<Element>>](unsafemutablebufferpointer/subscript(_:)-13u1d.md)
  Accesses a contiguous subrange of the buffer’s elements.
- [subscript(Int) -> Element](unsafemutablebufferpointer/subscript(_:)-9t9gq.md)
  Accesses the element at the specified position.
### Type Aliases
- [UnsafeMutableBufferPointer.Index](unsafemutablebufferpointer/index.md)
  A type that represents a position in the collection.
- [UnsafeMutableBufferPointer.Indices](unsafemutablebufferpointer/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [UnsafeMutableBufferPointer.SubSequence](unsafemutablebufferpointer/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/collection-implementations)*