# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Structures
- [String.Index](string/index.md)
  A position of a character or code unit in a string.
### Instance Properties
- [var endIndex: String.Index](string/endindex.md)
  A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var last: Self.Element?](string/last.md)
  The last element of the collection.
- [var startIndex: String.Index](string/startindex.md)
  The position of the first character in a nonempty string.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](string/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](string/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: String.Index, to: String.Index) -> Int](string/distance(from:to:).md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](string/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](string/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(String.Index, offsetBy: Int) -> String.Index](string/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(String.Index, offsetBy: Int, limitedBy: String.Index) -> String.Index?](string/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: String.Index) -> String.Index](string/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: String.Index) -> String.Index](string/index(before:).md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](string/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](string/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](string/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](string/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](string/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(Range<String.Index>) -> Substring](string/subscript(_:)-2so14.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(String.Index) -> Character](string/subscript(_:)-lc0v.md)
  Accesses the character at the given position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/bidirectionalcollection-implementations)*