# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](defaultindices/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](defaultindices/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](defaultindices/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func formIndex(before: inout DefaultIndices<Elements>.Index)](defaultindices/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(before: inout Self.Index)](defaultindices/formindex(before:)-6w7lf.md)
  Replaces the given index with its predecessor.
- [func index(before: DefaultIndices<Elements>.Index) -> DefaultIndices<Elements>.Index](defaultindices/index(before:).md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](defaultindices/joined(separator:)-5do0s.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](defaultindices/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](defaultindices/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](defaultindices/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](defaultindices/poplast.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](defaultindices/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](defaultindices/removelast(_:).md)
  Removes the given number of elements from the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/defaultindices/bidirectionalcollection-implementations)*