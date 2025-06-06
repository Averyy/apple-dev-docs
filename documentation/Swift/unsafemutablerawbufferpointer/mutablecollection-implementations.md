# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](unsafemutablerawbufferpointer/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](unsafemutablerawbufferpointer/partition(by:)-33su4.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](unsafemutablerawbufferpointer/partition(by:)-90pny.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](unsafemutablerawbufferpointer/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](unsafemutablerawbufferpointer/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](unsafemutablerawbufferpointer/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](unsafemutablerawbufferpointer/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](unsafemutablerawbufferpointer/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Int, Int)](unsafemutablerawbufferpointer/swapat(_:_:).md)
  Exchanges the byte values at the specified indices in this buffer’s memory.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<UnsafeMutableRawBufferPointer.Element>) throws -> R) rethrows -> R?](unsafemutablerawbufferpointer/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](unsafemutablerawbufferpointer/subscript(_:)-3g42.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Slice<Self>](unsafemutablerawbufferpointer/subscript(_:)-3i1y.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](unsafemutablerawbufferpointer/subscript(_:)-3kwnc.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](unsafemutablerawbufferpointer/subscript(_:)-3pmfu.md)
- [subscript(Range<Self.Index>) -> Self.SubSequence](unsafemutablerawbufferpointer/subscript(_:)-9v9lo.md)
- [subscript(Int) -> UnsafeMutableRawBufferPointer.Element](unsafemutablerawbufferpointer/subscript(_:)-u791.md)
  Accesses the byte at the given offset in the memory region as a `UInt8` value.
- [subscript(Range<Int>) -> UnsafeMutableRawBufferPointer.SubSequence](unsafemutablerawbufferpointer/subscript(_:)-znv7.md)
  Accesses the bytes in the specified memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/mutablecollection-implementations)*