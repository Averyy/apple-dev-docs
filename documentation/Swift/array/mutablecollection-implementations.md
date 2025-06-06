# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](array/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](array/partition(by:)-33stm.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](array/partition(by:)-90po8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](array/removesubranges(_:)-276ym.md)
  Removes the elements at the given indices.
- [func reverse()](array/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](array/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](array/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](array/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](array/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](array/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](array/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](array/withcontiguousmutablestorageifavailable(_:)-7398r.md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](array/subscript(_:)-3i28.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-3kwny.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](array/subscript(_:)-3pmfg.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](array/subscript(_:)-9v9l6.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/mutablecollection-implementations)*