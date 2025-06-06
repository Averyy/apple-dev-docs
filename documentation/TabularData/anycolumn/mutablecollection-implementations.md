# MutableCollection Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](anycolumn/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](anycolumn/partition(by:)-6pyre.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](anycolumn/partition(by:)-7fpjw.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](anycolumn/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](anycolumn/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](anycolumn/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](anycolumn/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<Comparator>(using: Comparator)](anycolumn/sort(using:)-68tuq.md)
  Sorts the collection using the given comparator to compare elements.
- [func sort<S, Comparator>(using: S)](anycolumn/sort(using:)-d15r.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func swapAt(Self.Index, Self.Index)](anycolumn/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](anycolumn/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](anycolumn/subscript(_:)-6as9f.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/mutablecollection-implementations)*