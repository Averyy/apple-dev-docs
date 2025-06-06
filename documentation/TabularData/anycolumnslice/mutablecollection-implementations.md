# MutableCollection Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](anycolumnslice/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](anycolumnslice/partition(by:)-5h4eh.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](anycolumnslice/partition(by:)-90301.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](anycolumnslice/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](anycolumnslice/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](anycolumnslice/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](anycolumnslice/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<Comparator>(using: Comparator)](anycolumnslice/sort(using:)-43qbc.md)
  Sorts the collection using the given comparator to compare elements.
- [func sort<S, Comparator>(using: S)](anycolumnslice/sort(using:)-781u0.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func swapAt(Self.Index, Self.Index)](anycolumnslice/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](anycolumnslice/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](anycolumnslice/subscript(_:)-6uodd.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/mutablecollection-implementations)*