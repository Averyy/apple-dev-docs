# init()

**Framework**: RealityKit  
**Kind**: init

Creates a new anchor entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency required init()
```

## See Also

- [convenience init(any Anchor)](anchorentity/init(_:)-8k2z3.md)
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
- [convenience init(world: float4x4)](anchorentity/init(world:)-4snw2.md)
  Creates an anchor entity with a target fixed at the given position in the scene.
- [convenience init(world: SIMD3<Float>)](anchorentity/init(world:)-u9qv.md)
  Creates an anchor entity with a target fixed at the given position in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/init())*