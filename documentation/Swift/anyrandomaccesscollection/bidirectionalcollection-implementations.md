# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](anyrandomaccesscollection/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](anyrandomaccesscollection/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](anyrandomaccesscollection/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func joined(separator: String) -> String](anyrandomaccesscollection/joined(separator:)-9vrqj.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](anyrandomaccesscollection/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](anyrandomaccesscollection/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](anyrandomaccesscollection/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](anyrandomaccesscollection/poplast.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](anyrandomaccesscollection/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](anyrandomaccesscollection/removelast(_:).md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](anyrandomaccesscollection/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyrandomaccesscollection/bidirectionalcollection-implementations)*