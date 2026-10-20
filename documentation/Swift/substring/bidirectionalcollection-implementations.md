# BidirectionalCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var last: Self.Element?](./last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](./difference%28from%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](./difference%28from,by%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Substring.Index, to: Substring.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](./droplast%28_%29.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(Substring.Index, offsetBy: Int) -> Substring.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(Substring.Index, offsetBy: Int, limitedBy: Substring.Index) -> Substring.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Substring.Index) -> Substring.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: Substring.Index) -> Substring.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./last%28where%29.md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](./lastindex%28of%29.md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](./poplast%28%29-7k3s0.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29-2gcne.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./removelast%28_%29-8r1d9.md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](./reversed%28%29.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](./suffix%28_%29.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(Range<Substring.Index>) -> Substring](./subscript%28_%29-6e3qj.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/bidirectionalcollection-implementations)*