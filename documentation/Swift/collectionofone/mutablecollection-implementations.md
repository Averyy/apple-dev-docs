# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](collectionofone/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](collectionofone/partition(by:)-1s0cl.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](collectionofone/partition(by:)-2ouy4.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](collectionofone/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](collectionofone/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](collectionofone/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](collectionofone/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](collectionofone/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](collectionofone/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](collectionofone/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Self.SubSequence](collectionofone/subscript(_:)-5ny44.md)
- [subscript<R>(R) -> Self.SubSequence](collectionofone/subscript(_:)-7b34k.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](collectionofone/subscript(_:)-7lp8k.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](collectionofone/subscript(_:)-82bqh.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Slice<Self>](collectionofone/subscript(_:)-8buws.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectionofone/mutablecollection-implementations)*