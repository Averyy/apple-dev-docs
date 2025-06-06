# MutableCollection Implementations

**Framework**: Foundation

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](data/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](data/partition(by:)-6ac65.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](data/partition(by:)-8lsit.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](data/removesubranges(_:)-2yy63.md)
  Removes the elements at the given indices.
- [func reverse()](data/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](data/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](data/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](data/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](data/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<S, Comparator>(using: S)](data/sort(using:)-1lwus.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func sort<Comparator>(using: Comparator)](data/sort(using:)-5xj3f.md)
  Sorts the collection using the given comparator to compare elements.
- [func swapAt(Self.Index, Self.Index)](data/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](data/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript<R>(R) -> Self.SubSequence](data/subscript(_:)-6fjxg.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](data/subscript(_:)-99re.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Self.SubSequence](data/subscript(_:)-aswc.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](data/subscript(_:)-fl4q.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/mutablecollection-implementations)*