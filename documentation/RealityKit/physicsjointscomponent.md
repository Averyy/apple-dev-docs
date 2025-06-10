# PhysicsJointsComponent

**Framework**: RealityKit  
**Kind**: struct

A component that stores physics joints which RealityKit simulates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct PhysicsJointsComponent
```

#### Overview

Add this component to an entity, or any child of an entity, that has a [`PhysicsSimulationComponent`](physicssimulationcomponent.md). All joints in the `PhysicsJointsComponent` need to reference entities under the same [`PhysicsSimulationComponent`](physicssimulationcomponent.md) tree.

Add a joint to the correct `PhysicsJointsComponent` instance by calling its `PhysicsJoint/addToSimulation()-886c4` method.

## Topics

### Initializers
- [init()](physicsjointscomponent/init.md)
  Creates a new physics joints component.
### Instance Properties
- [var joints: PhysicsJoints](physicsjointscomponent/joints.md)
  The set of joints the physics joints component stores.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Simulating physics joints in your RealityKit app](simulating-physics-joints-in-your-realitykit-app.md)
  Create realistic, connected motion using physics joints.
- [struct GeometricPin](geometricpin.md)
  A structure that identifies a local transform relative to an entity or entity’s animating skeletal joint.
- [struct GeometricPinsComponent](geometricpinscomponent.md)
  A component that stores a sequence of geometric pins.
- [protocol PhysicsJoint](physicsjoint.md)
  A type that describes physics joints.
- [struct EntityGeometricPins](entitygeometricpins.md)
  A structure that wraps all geometric pins an entity owns.
- [struct AttachedTransformComponent](attachedtransformcomponent.md)
  A component that stores an optional source pin owned by this entity and a target pin which this entity is attached to


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjointscomponent)*