# default

**Framework**: RealityKit  
**Kind**: property

The default collision group for objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
static let `default`: CollisionGroup
```

#### Discussion

If no [`CollisionFilter`](collisionfilter.md) is assigned to an entity, that entity will be part of this default collision group.

## See Also

- [static let all: CollisionGroup](collisiongroup/all.md)
  The collision group that represents all groups.
- [static let sceneUnderstanding: CollisionGroup](collisiongroup/sceneunderstanding.md)
  The default collision group for scene-understanding meshes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisiongroup/default)*