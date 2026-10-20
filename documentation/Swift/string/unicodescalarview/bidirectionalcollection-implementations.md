# BidirectionalCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: String.UnicodeScalarView.Index](./endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var last: Self.Element?](./last.md)
  The last element of the collection.
- [var startIndex: String.UnicodeScalarView.Index](./startindex.md)
  The position of the first Unicode scalar value if the string is nonempty.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](./difference%28from%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](./difference%28from,by%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: String.UnicodeScalarView.Index, to: String.UnicodeScalarView.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](./droplast%28_%29.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(String.UnicodeScalarView.Index, offsetBy: Int) -> String.UnicodeScalarView.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(String.UnicodeScalarView.Index, offsetBy: Int, limitedBy: String.UnicodeScalarView.Index) -> String.UnicodeScalarView.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: String.UnicodeScalarView.Index) -> String.UnicodeScalarView.Index](./index%28after%29.md)
  Returns the next consecutive location after `i`.
- [func index(before: String.UnicodeScalarView.Index) -> String.UnicodeScalarView.Index](./index%28before%29.md)
  Returns the previous consecutive location before `i`.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./last%28where%29.md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](./lastindex%28of%29.md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](./reversed%28%29.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](./suffix%28_%29.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(String.UnicodeScalarView.Index) -> Unicode.Scalar](./subscript%28_%29-2op53.md)
  Accesses the Unicode scalar value at the given position.
- [subscript(Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView.SubSequence](./subscript%28_%29-6aml8.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview/bidirectionalcollection-implementations)*