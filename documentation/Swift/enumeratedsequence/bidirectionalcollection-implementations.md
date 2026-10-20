# BidirectionalCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var last: Self.Element?](./last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](./difference%28from,by%29.md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](./distance%28from,to%29-90p1a.md)
- [func formIndex(before: inout Self.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](./index%28_,offsetby%29-5oheh.md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](./index%28_,offsetby,limitedby%29-3spm1.md)
- [func index(before: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./last%28where%29.md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./lastindex%28where%29.md)
  Returns the index of the last element in the collection that matches the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/bidirectionalcollection-implementations)*