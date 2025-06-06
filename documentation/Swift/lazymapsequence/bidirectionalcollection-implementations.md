# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](lazymapsequence/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](lazymapsequence/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](lazymapsequence/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazymapsequence/distance(from:to:)-3cd1e.md)
- [func formIndex(before: inout LazyMapSequence<Base, Element>.Index)](lazymapsequence/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(before: inout Self.Index)](lazymapsequence/formindex(before:)-8rmvx.md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazymapsequence/index(_:offsetby:)-ldgv.md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazymapsequence/index(_:offsetby:limitedby:)-niw7.md)
- [func index(before: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index](lazymapsequence/index(before:).md)
  A value less than or equal to the number of elements in the collection.
- [func joined(separator: String) -> String](lazymapsequence/joined(separator:)-4i6uz.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](lazymapsequence/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](lazymapsequence/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazymapsequence/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/bidirectionalcollection-implementations)*