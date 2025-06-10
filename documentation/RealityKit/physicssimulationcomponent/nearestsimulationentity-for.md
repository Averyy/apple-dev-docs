# nearestSimulationEntity(for:)

**Framework**: RealityKit  
**Kind**: method

Obtains the entity containing the physics simulation origin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
static func nearestSimulationEntity(for entity: Entity) -> Entity?
```

#### Return Value

The entity containing the physics simulation origin or `nil` if the entity doesn’t have a parent object in the scene.

#### Discussion

The simulation origin is the nearest parent object where a [`PhysicsSimulationComponent`](physicssimulationcomponent.md) exists, or the root entity (normally the anchor) where the default simulation is embedded.

## Parameters

- `entity`: The entity to find the physics simulation origin for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationcomponent/nearestsimulationentity(for:))*