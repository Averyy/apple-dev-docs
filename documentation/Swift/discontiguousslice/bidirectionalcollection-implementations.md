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
- [func formIndex(before: inout Self.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(before: DiscontiguousSlice<Base>.Index) -> DiscontiguousSlice<Base>.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](./joined%28separator%29-4yy0x.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/bidirectionalcollection-implementations)*