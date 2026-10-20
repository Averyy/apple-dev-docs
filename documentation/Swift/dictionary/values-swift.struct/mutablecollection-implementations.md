# MutableCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](./movesubranges%28_,to%29.md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](./partition%28by%29.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](./swapat%28_,_%29-18i76.md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29.md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/mutablecollection-implementations)*