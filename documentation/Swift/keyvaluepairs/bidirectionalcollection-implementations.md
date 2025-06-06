# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](keyvaluepairs/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](keyvaluepairs/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](keyvaluepairs/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](keyvaluepairs/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](keyvaluepairs/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](keyvaluepairs/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](keyvaluepairs/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](keyvaluepairs/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs/bidirectionalcollection-implementations)*