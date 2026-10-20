# MutableCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](./movesubranges%28_,to%29.md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-2g3t0.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-2uabq.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](./removesubranges%28_%29-5ci4m.md)
  Removes the elements at the given indices.
- [func reverse()](./reverse%28%29.md)
  Reverses the elements of the collection in place.
- [func shuffle()](./shuffle%28%29.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](./shuffle%28using%29.md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](./sort%28%29.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](./sort%28by%29.md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](./swapat%28_,_%29.md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29.md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29-5k8vo.md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-17v9t.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](./subscript%28_%29-27a3j.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](./subscript%28_%29-6knxt.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-7ribf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/mutablecollection-implementations)*