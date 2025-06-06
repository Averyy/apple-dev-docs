# BidirectionalCollection Implementations

**Framework**: MusicKit

## Topics

### Instance Properties
- [var last: Self.Element?](applicationmusicplayer/queue-swift.class/entries-swift.struct/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](applicationmusicplayer/queue-swift.class/entries-swift.struct/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](applicationmusicplayer/queue-swift.class/entries-swift.struct/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](applicationmusicplayer/queue-swift.class/entries-swift.struct/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](applicationmusicplayer/queue-swift.class/entries-swift.struct/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](applicationmusicplayer/queue-swift.class/entries-swift.struct/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](applicationmusicplayer/queue-swift.class/entries-swift.struct/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/bidirectionalcollection-implementations)*