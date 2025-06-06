# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](dictionary/values-swift.struct/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](dictionary/values-swift.struct/partition(by:).md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func swapAt(Self.Index, Self.Index)](dictionary/values-swift.struct/swapat(_:_:)-18i76.md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](dictionary/values-swift.struct/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/mutablecollection-implementations)*