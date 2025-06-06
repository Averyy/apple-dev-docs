# look(at:from:upVector:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Positions and orients the entity to look at a target from a given position.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func look(at target: SIMD3<Float>, from position: SIMD3<Float>, upVector: SIMD3<Float> = SIMD3<Float>(0, 1, 0), relativeTo referenceEntity: Entity?)
```

#### Discussion

You can use this method on any entity, but it’s particularly useful for orienting cameras and lights to aim at a particular point in space.

## Parameters

- `target`: The target position to look at.
- `position`: The new position of the entity.
- `upVector`: The up direction of the entity after moving.
- `referenceEntity`: The entity that defines a frame of reference. Set this to    to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/look(at:from:upvector:relativeto:))*