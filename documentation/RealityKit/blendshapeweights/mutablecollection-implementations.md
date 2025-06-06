# MutableCollection Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](blendshapeweights/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](blendshapeweights/partition(by:)-9co72.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](blendshapeweights/partition(by:)-9y72q.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func reverse()](blendshapeweights/reverse.md)
  Reverses the elements of the collection in place.
- [func swapAt(Self.Index, Self.Index)](blendshapeweights/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](blendshapeweights/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweights/mutablecollection-implementations)*