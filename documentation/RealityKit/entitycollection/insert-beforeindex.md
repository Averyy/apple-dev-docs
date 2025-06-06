# insert(_:beforeIndex:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Adds the specified entity to this collection directly before the entity at the given index. If the entity is already located before the index, the collection will not change.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func insert(_ entity: Entity, beforeIndex index: Int)
```

#### Discussion

> **Note**: This operation can invalidate the index order of any extant entities.

This operation can invalidate the index order of any extant entities.

## Parameters

- `entity`: The entity to add to the collection.
- `index`: The index of an entity to insert in front   of. If   is provided, the entity   will be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection/insert(_:beforeindex:))*