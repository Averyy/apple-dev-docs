# MutableCollection Implementations

**Framework**: TabularData

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](dataframe/rows-swift.struct/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](dataframe/rows-swift.struct/partition(by:)-jit0.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](dataframe/rows-swift.struct/partition(by:)-ni38.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](dataframe/rows-swift.struct/reverse.md)
  Reverses the elements of the collection in place.
- [func swapAt(Self.Index, Self.Index)](dataframe/rows-swift.struct/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](dataframe/rows-swift.struct/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](dataframe/rows-swift.struct/subscript(_:)-3c8l4.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-47kxi.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-5beln.md)
- [subscript<R>(R) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-9yafe.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/mutablecollection-implementations)*