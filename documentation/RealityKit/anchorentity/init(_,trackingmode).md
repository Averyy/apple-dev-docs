# init(_:trackingMode:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(_ target: AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode)
```

## See Also

### Creating an anchor
- [init()](./init%28%29.md)
  Creates a new anchor entity.
- [convenience init(any Anchor)](./init%28_%29-9vipc.md)
- [init(AnchoringComponent.Target)](./init%28_%29-9rdwu.md)
  Creates an anchor entity targeting a particular kind of anchor.
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode, physicsSimulation: AnchoringComponent.PhysicsSimulation)](./init%28_,trackingmode,physicssimulation%29.md)
- [convenience init(anchor: ARAnchor)](./init%28anchor%29.md)
  Creates an anchor entity that uses an existing AR anchor.
- [convenience init(plane: AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](./init%28plane,classification,minimumbounds%29.md)
  Creates an anchor entity that targets a plane with the given characteristics.
- [convenience init(raycastResult: ARRaycastResult)](./init%28raycastresult%29.md)
  Creates an anchor entity using the information about a real-world surface discovered using a ray-cast query.
- [convenience init(world: float4x4)](./init%28world%29-4snw2.md)
  Creates an anchor entity with a target fixed at the given position in the scene.
- [convenience init(world: SIMD3<Float>)](./init%28world%29-u9qv.md)
  Creates an anchor entity with a target fixed at the given position in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/init(_:trackingmode:))*