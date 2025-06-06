# MutableCollection Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func moveSubranges(RangeSet<Self.Index>, to: Self.Index) -> Range<Self.Index>](slice/movesubranges(_:to:).md)
  Moves the elements in the given subranges to just before the element at the specified index.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](slice/partition(by:)-7efo8.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](slice/partition(by:)-7n9yj.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func removeSubranges(RangeSet<Self.Index>)](slice/removesubranges(_:)-20t3r.md)
  Removes the elements at the given indices.
- [func reverse()](slice/reverse.md)
  Reverses the elements of the collection in place.
- [func shuffle()](slice/shuffle.md)
  Shuffles the collection in place.
- [func shuffle<T>(using: inout T)](slice/shuffle(using:).md)
  Shuffles the collection in place, using the given generator as a source for randomness.
- [func sort()](slice/sort.md)
  Sorts the collection in place.
- [func sort(by: (Self.Element, Self.Element) throws -> Bool) rethrows](slice/sort(by:).md)
  Sorts the collection in place, using the given predicate as the comparison between elements.
- [func swapAt(Self.Index, Self.Index)](slice/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Slice<Base>.Element>) throws -> R) rethrows -> R?](slice/withcontiguousmutablestorageifavailable(_:)-2ual.md)
  Executes a closure on the collection’s contiguous storage.
### Subscripts
- [subscript(Range<Self.Index>) -> Self.SubSequence](slice/subscript(_:)-2elba.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](slice/subscript(_:)-3p9dc.md)
- [subscript<R>(R) -> Self.SubSequence](slice/subscript(_:)-4f8ky.md)
- [subscript(Range<Slice<Base>.Index>) -> Slice<Base>](slice/subscript(_:)-87kqd.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Slice<Self>](slice/subscript(_:)-8pq5s.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Range<Self.Index>) -> Slice<Self>](slice/subscript(_:)-uq47.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(Slice<Base>.Index) -> Base.Element](slice/subscript(_:)-z7ny.md)
  Accesses the element at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/mutablecollection-implementations)*