# init(_:trackingMode:physicsSimulation:)

**Framework**: RealityKit  
**Kind**: init

Creates an anchoring component for a given target, tracking mode and physics simulation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
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

- [init(AnchoringComponent.Target)](anchoringcomponent/init(_:)-2wng6.md)
  Creates an anchoring component for a given target.
- [init(_:trackingMode:)](anchoringcomponent/init(_:trackingmode:).md)
- [init(ARAnchor)](anchoringcomponent/init(_:)-5dney.md)
  Creates an anchoring component with the given AR anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/init(_:trackingmode:physicssimulation:))*