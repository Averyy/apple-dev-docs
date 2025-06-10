# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Int](unsafebufferpointer/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](unsafebufferpointer/first.md)
  The first element of the collection.
- [var indices: Range<Int>](unsafebufferpointer/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](unsafebufferpointer/isempty.md)
  A Boolean value indicating whether the buffer is empty.
- [var startIndex: Int](unsafebufferpointer/startindex.md)
  The index of the first element in a nonempty buffer.
- [var underestimatedCount: Int](unsafebufferpointer/underestimatedcount-4ggs2.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Int, to: Int) -> Int](unsafebufferpointer/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsafebufferpointer/drop(while:)-37wp5.md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](unsafebufferpointer/dropfirst(_:)-1rupy.md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](unsafebufferpointer/droplast(_:)-6rw21.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](unsafebufferpointer/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](unsafebufferpointer/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](unsafebufferpointer/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](unsafebufferpointer/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Int)](unsafebufferpointer/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Int, offsetBy: Int) -> Int](unsafebufferpointer/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](unsafebufferpointer/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](unsafebufferpointer/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](unsafebufferpointer/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](unsafebufferpointer/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](unsafebufferpointer/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](unsafebufferpointer/map(_:)-5p6pc.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](unsafebufferpointer/prefix(_:)-1n68g.md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](unsafebufferpointer/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](unsafebufferpointer/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](unsafebufferpointer/prefix(while:)-3ariq.md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](unsafebufferpointer/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](unsafebufferpointer/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](unsafebufferpointer/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](unsafebufferpointer/split(maxsplits:omittingemptysubsequences:whereseparator:)-4pbpp.md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](unsafebufferpointer/split(separator:maxsplits:omittingemptysubsequences:)-3dglg.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](unsafebufferpointer/suffix(_:)-qdda.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](unsafebufferpointer/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<Int>) -> Slice<UnsafeBufferPointer<Element>>](unsafebufferpointer/subscript(_:)-6ynnu.md)
  Accesses a contiguous subrange of the buffer’s elements.
- [subscript(Int) -> Element](unsafebufferpointer/subscript(_:)-9vykr.md)
  Accesses the element at the specified position.
### Type Aliases
- [UnsafeBufferPointer.Index](unsafebufferpointer/index.md)
  A type that represents a position in the collection.
- [UnsafeBufferPointer.Indices](unsafebufferpointer/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [UnsafeBufferPointer.SubSequence](unsafebufferpointer/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafebufferpointer/collection-implementations)*