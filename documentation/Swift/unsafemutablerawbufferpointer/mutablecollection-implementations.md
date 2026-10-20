# MutableCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](./movesubranges%28_,to%29.md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-33su4.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-90pny.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
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
- [func swapAt(Int, Int)](./swapat%28_,_%29.md)
  Exchanges the byte values at the specified indices in this buffer’s memory.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<UnsafeMutableRawBufferPointer.Element>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29.md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](./subscript%28_%29-3g42.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Slice<Self>](./subscript%28_%29-3i1y.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-3kwnc.md)
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-3pmfu.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](./subscript%28_%29-9v9lo.md)
- [subscript(Int) -> UnsafeMutableRawBufferPointer.Element](./subscript%28_%29-u791.md)
  Accesses the byte at the given offset in the memory region as a `UInt8` value.
- [subscript(Range<Int>) -> UnsafeMutableRawBufferPointer.SubSequence](./subscript%28_%29-znv7.md)
  Accesses the bytes in the specified memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations)*