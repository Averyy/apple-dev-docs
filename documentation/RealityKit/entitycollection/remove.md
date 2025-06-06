# remove(_:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Removes the entity from the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func remove(_ entity: Entity)
```

#### Discussion

> **Note**: This operation can invalidate the index order of any remaining entities.

This operation can invalidate the index order of any remaining entities.

## Parameters

- `entity`: The entity to remove from the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection/remove(_:))*