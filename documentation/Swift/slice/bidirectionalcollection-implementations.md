# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](slice/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](slice/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](slice/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func formIndex(before: inout Slice<Base>.Index)](slice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(before: inout Self.Index)](slice/formindex(before:)-d9pr.md)
  Replaces the given index with its predecessor.
- [func index(before: Slice<Base>.Index) -> Slice<Base>.Index](slice/index(before:).md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](slice/joined(separator:)-6sxlg.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](slice/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](slice/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](slice/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](slice/poplast-7zlp7.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](slice/removelast-29ty4.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](slice/removelast(_:)-4ijd6.md)
  Removes the given number of elements from the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/bidirectionalcollection-implementations)*