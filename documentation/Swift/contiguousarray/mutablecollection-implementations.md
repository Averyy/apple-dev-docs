# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](contiguousarray/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](contiguousarray/partition(by:)-2g3t0.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](contiguousarray/partition(by:)-2uabq.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](contiguousarray/removesubranges(_:)-5ci4m.md)
  Removes the elements at the given indices.
- [func reverse()](contiguousarray/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](contiguousarray/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](contiguousarray/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](contiguousarray/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](contiguousarray/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](contiguousarray/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](contiguousarray/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](contiguousarray/withcontiguousmutablestorageifavailable(_:)-5k8vo.md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](contiguousarray/subscript(_:)-17v9t.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](contiguousarray/subscript(_:)-27a3j.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](contiguousarray/subscript(_:)-6knxt.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](contiguousarray/subscript(_:)-7ribf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/mutablecollection-implementations)*