# MutableCollection Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](column/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](column/partition(by:)-7sneq.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](column/partition(by:)-li.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](column/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](column/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](column/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](column/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<S, Comparator>(using: S)](column/sort(using:)-22f7y.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func sort<Comparator>(using: Comparator)](column/sort(using:)-91ejq.md)
  Sorts the collection using the given comparator to compare elements.
- [func swapAt(Self.Index, Self.Index)](column/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](column/withcontiguousmutablestorageifavailable(_:)-30xzy.md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement?>) throws -> R) rethrows -> R?](column/withcontiguousmutablestorageifavailable(_:)-77itz.md)
  This method always returns `nil` without calling `body`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/mutablecollection-implementations)*