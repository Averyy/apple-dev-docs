# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](arrayslice/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](arrayslice/partition(by:)-2s919.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](arrayslice/partition(by:)-706dh.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](arrayslice/removesubranges(_:)-k50b.md)
  Removes the elements at the given indices.
- [func reverse()](arrayslice/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](arrayslice/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](arrayslice/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](arrayslice/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](arrayslice/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](arrayslice/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](arrayslice/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](arrayslice/withcontiguousmutablestorageifavailable(_:)-5vekj.md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](arrayslice/subscript(_:)-3f18y.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](arrayslice/subscript(_:)-6gtfn.md)
- [subscript<R>(R) -> Self.SubSequence](arrayslice/subscript(_:)-7gag3.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](arrayslice/subscript(_:)-7xg8e.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/mutablecollection-implementations)*