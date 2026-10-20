# init(world:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an anchor entity with a target fixed at the given position in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency convenience init(world transform: float4x4)
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(world position: SIMD3<Float>)
```

## Parameters

- `transform`: The transform with which to initialize the world target.

## See Also

### Creating an anchor
- [init()](./init%28%29.md)
  Creates a new anchor entity.
- [convenience init(any Anchor)](./init%28_%29-9vipc.md)
- [init(AnchoringComponent.Target)](./init%28_%29-9rdwu.md)
  Creates an anchor entity targeting a particular kind of anchor.
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode)](./init%28_,trackingmode%29.md)
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode, physicsSimulation: AnchoringComponent.PhysicsSimulation)](./init%28_,trackingmode,physicssimulation%29.md)
- [convenience init(anchor: ARAnchor)](./init%28anchor%29.md)
  Creates an anchor entity that uses an existing AR anchor.
- [convenience init(plane: AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](./init%28plane,classification,minimumbounds%29.md)
  Creates an anchor entity that targets a plane with the given characteristics.
- [convenience init(raycastResult: ARRaycastResult)](./init%28raycastresult%29.md)
  Creates an anchor entity using the information about a real-world surface discovered using a ray-cast query.
- [convenience init(world: SIMD3<Float>)](./init%28world%29-u9qv.md)
  Creates an anchor entity with a target fixed at the given position in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/init(world:)-4snw2)*