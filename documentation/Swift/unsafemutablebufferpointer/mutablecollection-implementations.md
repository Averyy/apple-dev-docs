# MutableCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](./movesubranges%28_,to%29.md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-33su1.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29-90pnv.md)
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
  Exchanges the values at the specified indices of the buffer.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29.md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29-73994.md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/mutablecollection-implementations)*