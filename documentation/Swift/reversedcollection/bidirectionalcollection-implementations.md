# BidirectionalCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Structures
- [ReversedCollection.Index](./index.md)
  An index that traverses the same positions as an underlying index, with inverted traversal direction.
### Instance Properties
- [var last: Self.Element?](./last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](./difference%28from%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](./difference%28from,by%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: ReversedCollection<Base>.Index, to: ReversedCollection<Base>.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](./droplast%28_%29.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(ReversedCollection<Base>.Index, offsetBy: Int) -> ReversedCollection<Base>.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(ReversedCollection<Base>.Index, offsetBy: Int, limitedBy: ReversedCollection<Base>.Index) -> ReversedCollection<Base>.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: ReversedCollection<Base>.Index) -> ReversedCollection<Base>.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: ReversedCollection<Base>.Index) -> ReversedCollection<Base>.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](./joined%28separator%29-3e82c.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./last%28where%29.md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](./lastindex%28of%29.md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func suffix(Int) -> Self.SubSequence](./suffix%28_%29.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/reversedcollection/bidirectionalcollection-implementations)*