# Entity.ComponentSet.Indices

**Framework**: RealityKit  
**Kind**: struct

A type that represents the indices that are valid for subscripting the collection, in ascending order.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Indices
```

## Topics

### Instance Properties
- [var endIndex: Entity.ComponentSet.Indices.Index](entity/componentset/indices-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Entity.ComponentSet.Indices](entity/componentset/indices-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Entity.ComponentSet.Indices.Index](entity/componentset/indices-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Entity.ComponentSet.Indices.Index, to: Entity.ComponentSet.Indices.Index) -> Int](entity/componentset/indices-swift.struct/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout Entity.ComponentSet.Indices.Index)](entity/componentset/indices-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(after: Entity.ComponentSet.Indices.Index) -> Entity.ComponentSet.Indices.Index](entity/componentset/indices-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
### Subscripts
- [subscript(Entity.ComponentSet.Indices.Index) -> Entity.ComponentSet.Indices.Index](entity/componentset/indices-swift.struct/subscript(_:)-4onvj.md)
  Accesses the element at the specified position.
- [subscript(Range<Entity.ComponentSet.Indices.Index>) -> Entity.ComponentSet.Indices](entity/componentset/indices-swift.struct/subscript(_:)-8o964.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [Entity.ComponentSet.Indices.Element](entity/componentset/indices-swift.struct/element.md)
  A type representing the sequence’s elements.
- [Entity.ComponentSet.Indices.Index](entity/componentset/indices-swift.struct/index.md)
  A type that represents a position in the collection.
- [Entity.ComponentSet.Indices.Indices](entity/componentset/indices-swift.struct/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Entity.ComponentSet.Indices.Iterator](entity/componentset/indices-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Entity.ComponentSet.Indices.SubSequence](entity/componentset/indices-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](entity/componentset/indices-swift.struct/collection-implementations.md)
- [Sequence Implementations](entity/componentset/indices-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/indices-swift.struct)*