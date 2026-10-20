# init(_:trackingMode:physicsSimulation:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an anchoring component for a given target, tracking mode and physics simulation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(_ target: AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode, physicsSimulation: AnchoringComponent.PhysicsSimulation = .isolated)
```

## Parameters

- `target`: The kind of real world object to target.
- `trackingMode`: The tracking mode of the entity.
- `physicsSimulation`: The physics simulation space the entity will be in.

## See Also

### Creating an anchoring component
- [init(_:)](./init%28_%29.md)
  Creates an anchoring component with the given AR anchor.
- [init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode)](./init%28_,trackingmode%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/init(_:trackingmode:physicssimulation:))*