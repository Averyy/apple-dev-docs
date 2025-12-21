# init(world:)

**Framework**: RealityKit  
**Kind**: init

Creates an anchor entity with a target fixed at the given position in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(world transform: float4x4)
```

## Parameters

- `transform`: The transform with which to initialize the world target.

## See Also

- [init()](anchorentity/init.md)
  Creates a new anchor entity.
- [init(AnchoringComponent.Target)](anchorentity/init(_:)-9rdwu.md)
  Creates an anchor entity targeting a particular kind of anchor.
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode)](anchorentity/init(_:trackingmode:).md)
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode, physicsSimulation: AnchoringComponent.PhysicsSimulation)](anchorentity/init(_:trackingmode:physicssimulation:).md)
- [convenience init(anchor: ARAnchor)](anchorentity/init(anchor:).md)
  Creates an anchor entity that uses an existing AR anchor.
- [convenience init(plane: AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](anchorentity/init(plane:classification:minimumbounds:).md)
  Creates an anchor entity that targets a plane with the given characteristics.
- [convenience init(raycastResult: ARRaycastResult)](anchorentity/init(raycastresult:).md)
  Creates an anchor entity using the information about a real-world surface discovered using a ray-cast query.
- [convenience init(world: SIMD3<Float>)](anchorentity/init(world:)-u9qv.md)
  Creates an anchor entity with a target fixed at the given position in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/init(world:)-4snw2)*