# SceneUnderstandingComponent.EntityType.meshChunk

**Framework**: RealityKit  
**Kind**: case

An entity that models the physical shape of the environment within a given cubic region.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 27.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case meshChunk
```

#### Discussion

When `SpotLightComponent.SurroundingsLight` or `PointLightComponent.SurroundingsLight` is enabled:

- On visionOS, RealityKit automatically selects the opaque meshes that intersect the bounding box of the entity’s mesh and illuminates them with surroundings light in a progressive immersive space.
- On macOS, surroundings light illuminates the entity’s mesh.

When [`GroundingShadowComponent`](groundingshadowcomponent.md) is enabled:

- On visionOS, the entity’s mesh receives grounding shadows in a progressive immersive space.
- On macOS, the entity’s mesh receives grounding shadows.

## See Also

- [SceneUnderstandingComponent.EntityType.face](sceneunderstandingcomponent/entitytype-swift.enum/face.md)
  An entity that models a face that the framework detects in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneunderstandingcomponent/entitytype-swift.enum/meshchunk)*