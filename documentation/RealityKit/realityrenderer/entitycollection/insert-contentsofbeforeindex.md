# insert(contentsOf:beforeIndex:)

**Framework**: Realitykit  
**Kind**: method

Adds the specified sequence of entities to this collection in order, directly before the entity at the given index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
mutating func insert<S>(contentsOf sequence: S, beforeIndex index: Int) where S : Sequence, S.Element : Entity
```

#### Discussion

> **Note**: This operation can invalidate the index order of any extant entities.

## Parameters

- `sequence`: A sequence of entities to add to the collection.
- `index`: The index of an entity to insert in front   of. If   is provided, the   entities will be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/entitycollection/insert(contentsof:beforeindex:))*