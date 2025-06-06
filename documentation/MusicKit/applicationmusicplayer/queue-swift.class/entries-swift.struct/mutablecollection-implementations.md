# MutableCollection Implementations

**Framework**: MusicKit

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](applicationmusicplayer/queue-swift.class/entries-swift.struct/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/partition(by:)-5byqr.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/partition(by:)-nz5z.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](applicationmusicplayer/queue-swift.class/entries-swift.struct/removesubranges(_:)-5qugs.md)
  Removes the elements at the given indices.
- [func reverse()](applicationmusicplayer/queue-swift.class/entries-swift.struct/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](applicationmusicplayer/queue-swift.class/entries-swift.struct/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](applicationmusicplayer/queue-swift.class/entries-swift.struct/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](applicationmusicplayer/queue-swift.class/entries-swift.struct/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<S, Comparator>(using: S)](applicationmusicplayer/queue-swift.class/entries-swift.struct/sort(using:)-2vim9.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func sort<Comparator>(using: Comparator)](applicationmusicplayer/queue-swift.class/entries-swift.struct/sort(using:)-875wx.md)
  Sorts the collection using the given comparator to compare elements.
- [func swapAt(Self.Index, Self.Index)](applicationmusicplayer/queue-swift.class/entries-swift.struct/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](applicationmusicplayer/queue-swift.class/entries-swift.struct/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](applicationmusicplayer/queue-swift.class/entries-swift.struct/subscript(_:)-2jq11.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Self.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/subscript(_:)-2yc0q.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/subscript(_:)-6nrcv.md)
- [subscript<R>(R) -> Self.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/subscript(_:)-8yobl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/mutablecollection-implementations)*