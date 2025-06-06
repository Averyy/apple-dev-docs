# DiscontiguousSlice

**Framework**: Swift  
**Kind**: struct

A collection wrapper that provides access to the elements of a collection, indexed by a set of indices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DiscontiguousSlice<Base> where Base : Collection
```

## Topics

### Instance Properties
- [var base: Base](discontiguousslice/base.md)
  The collection that the indexed collection wraps.
- [let subranges: RangeSet<Base.Index>](discontiguousslice/subranges.md)
  The set of subranges that are available through this discontiguous slice.
### Subscripts
- [subscript(DiscontiguousSlice<Base>.Index) -> Base.Element](discontiguousslice/subscript(_:)-1j7n7.md)
  Accesses the element at the specified position.
### Default Implementations
- [BidirectionalCollection Implementations](discontiguousslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](discontiguousslice/collection-implementations.md)
- [CustomStringConvertible Implementations](discontiguousslice/customstringconvertible-implementations.md)
- [Equatable Implementations](discontiguousslice/equatable-implementations.md)
- [Hashable Implementations](discontiguousslice/hashable-implementations.md)
- [Sequence Implementations](discontiguousslice/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice)*