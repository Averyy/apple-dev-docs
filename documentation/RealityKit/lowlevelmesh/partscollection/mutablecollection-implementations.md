# MutableCollection Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](lowlevelmesh/partscollection/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](lowlevelmesh/partscollection/partition(by:)-28ghl.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](lowlevelmesh/partscollection/partition(by:)-7mlra.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](lowlevelmesh/partscollection/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](lowlevelmesh/partscollection/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](lowlevelmesh/partscollection/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](lowlevelmesh/partscollection/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func sort<Comparator>(using: Comparator)](lowlevelmesh/partscollection/sort(using:)-20e8f.md)
  Sorts the collection using the given comparator to compare elements.
- [func sort<S, Comparator>(using: S)](lowlevelmesh/partscollection/sort(using:)-4qvaq.md)
  Sorts the collection using the given array of `SortComparator`s to compare elements.
- [func swapAt(Self.Index, Self.Index)](lowlevelmesh/partscollection/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](lowlevelmesh/partscollection/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(LowLevelMesh.PartsCollection.Index) -> LowLevelMesh.Part](lowlevelmesh/partscollection/subscript(_:).md)
  Accesses the element at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/partscollection/mutablecollection-implementations)*