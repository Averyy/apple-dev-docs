# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](unsafemutablebufferpointer/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](unsafemutablebufferpointer/partition(by:)-33su1.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](unsafemutablebufferpointer/partition(by:)-90pnv.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](unsafemutablebufferpointer/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](unsafemutablebufferpointer/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](unsafemutablebufferpointer/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](unsafemutablebufferpointer/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](unsafemutablebufferpointer/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Int, Int)](unsafemutablebufferpointer/swapat(_:_:).md)
  Exchanges the values at the specified indices of the buffer.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](unsafemutablebufferpointer/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](unsafemutablebufferpointer/withcontiguousmutablestorageifavailable(_:)-73994.md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/mutablecollection-implementations)*