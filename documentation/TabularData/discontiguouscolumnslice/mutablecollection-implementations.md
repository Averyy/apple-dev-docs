# MutableCollection Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](discontiguouscolumnslice/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](discontiguouscolumnslice/partition(by:)-3lx5r.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](discontiguouscolumnslice/partition(by:)-51ifb.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](discontiguouscolumnslice/reverse.md)
  Reverses the elements of the collection in place.
- [func swapAt(Self.Index, Self.Index)](discontiguouscolumnslice/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](discontiguouscolumnslice/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](discontiguouscolumnslice/subscript(_:)-7pxg6.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/mutablecollection-implementations)*