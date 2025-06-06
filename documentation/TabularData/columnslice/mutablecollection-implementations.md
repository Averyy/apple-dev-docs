# MutableCollection Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](columnslice/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](columnslice/partition(by:)-5cldl.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](columnslice/partition(by:)-5nzbc.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](columnslice/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](columnslice/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](columnslice/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](columnslice/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<S, Comparator>(using: S)](columnslice/sort(using:)-65eef.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func sort<Comparator>(using: Comparator)](columnslice/sort(using:)-8zuii.md)
  Sorts the collection using the given comparator to compare elements.
- [func swapAt(Self.Index, Self.Index)](columnslice/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](columnslice/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/mutablecollection-implementations)*