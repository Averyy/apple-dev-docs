# BidirectionalCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: AnyBidirectionalCollection<Element>.Index](./endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var last: Self.Element?](./last.md)
  The last element of the collection.
- [var startIndex: AnyBidirectionalCollection<Element>.Index](./startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](./difference%28from%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](./difference%28from,by%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: AnyBidirectionalCollection<Element>.Index, to: AnyBidirectionalCollection<Element>.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func formIndex(after: inout AnyBidirectionalCollection<Element>.Index)](./formindex%28after%29.md)
  Replaces the given index with its successor.
- [func formIndex(before: inout AnyBidirectionalCollection<Element>.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(AnyBidirectionalCollection<Element>.Index, offsetBy: Int) -> AnyBidirectionalCollection<Element>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(AnyBidirectionalCollection<Element>.Index, offsetBy: Int, limitedBy: AnyBidirectionalCollection<Element>.Index) -> AnyBidirectionalCollection<Element>.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: AnyBidirectionalCollection<Element>.Index) -> AnyBidirectionalCollection<Element>.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: AnyBidirectionalCollection<Element>.Index) -> AnyBidirectionalCollection<Element>.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](./joined%28separator%29-6ag5z.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./last%28where%29.md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](./lastindex%28of%29.md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](./poplast%28%29.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./removelast%28_%29.md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](./reversed%28%29.md)
  Returns a view presenting the elements of the collection in reverse order.
### Subscripts
- [subscript(AnyBidirectionalCollection<Element>.Index) -> Element](./subscript%28_%29-95c1r.md)
  Accesses the element indicated by `position`.
- [subscript(Range<AnyBidirectionalCollection<Element>.Index>) -> AnyBidirectionalCollection<Element>.SubSequence](./subscript%28_%29-9b37e.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anybidirectionalcollection/bidirectionalcollection-implementations)*