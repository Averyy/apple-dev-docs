# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](emptycollection/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](emptycollection/partition(by:)-37csa.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](emptycollection/partition(by:)-4cd8k.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](emptycollection/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](emptycollection/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](emptycollection/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](emptycollection/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](emptycollection/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](emptycollection/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](emptycollection/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](emptycollection/subscript(_:)-1atow.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](emptycollection/subscript(_:)-27szq.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](emptycollection/subscript(_:)-6sv7g.md)
- [subscript<R>(R) -> Self.SubSequence](emptycollection/subscript(_:)-9ngyd.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/mutablecollection-implementations)*