# Entity.CoordinateSpaceReference.scene

**Framework**: RealityKit  
**Kind**: case

A reference to an entity’s parent window scene.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case scene
```

#### Discussion

You can use this enum case to get an entity’s relative transform in its parented window scene:

```swift
let transformInWindowSpace = windowEntity.transformMatrix(relativeTo: .scene)
```

> **Note**: If an entity is parented under an , calling [`transformMatrix(relativeTo:)`](entity/transformmatrix(relativeto:).md) with the case `scene` returns `nil`.

If an entity is parented under an , calling [`transformMatrix(relativeTo:)`](entity/transformmatrix(relativeto:).md) with the case `scene` returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/coordinatespacereference/scene)*