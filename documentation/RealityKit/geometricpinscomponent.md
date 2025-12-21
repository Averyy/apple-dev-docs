# GeometricPinsComponent

**Framework**: RealityKit  
**Kind**: struct

A component that stores a sequence of geometric pins.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct GeometricPinsComponent
```

#### Overview

Add, inspect, and remove geometric pins that belong to the entity that owns an instance of `GeometricPinsComponent` by accessing its [`pins`](entity/pins.md) property.

## Topics

### Initializers
- [init()](geometricpinscomponent/init.md)
  Creates a geometric pins component with an empty sequence of pins.
### Instance Properties
- [var pins: Set<GeometricPin>](geometricpinscomponent/pins.md)
  The sequence of geometric pins the component owns.
### Instance Methods
- [func removePin(named: String) -> GeometricPin?](geometricpinscomponent/removepin(named:).md)
  Removes the pin associated with the name.
- [func set(pin: GeometricPin)](geometricpinscomponent/set(pin:).md)
  Adds a pin to the collection.
### Subscripts
- [subscript(String) -> GeometricPin?](geometricpinscomponent/subscript(_:).md)
  Retrieves the pin by its name.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Simulating physics joints in your RealityKit app](simulating-physics-joints-in-your-realitykit-app.md)
  Create realistic, connected motion using physics joints.
- [struct GeometricPin](geometricpin.md)
  A structure that identifies a local transform relative to an entity or entity’s animating skeletal joint.
- [protocol PhysicsJoint](physicsjoint.md)
  A type that describes physics joints.
- [struct PhysicsJointsComponent](physicsjointscomponent.md)
  A component that stores physics joints which RealityKit simulates.
- [struct EntityGeometricPins](entitygeometricpins.md)
  A structure that wraps all geometric pins an entity owns.
- [struct AttachedTransformComponent](attachedtransformcomponent.md)
  A component that stores an optional source pin owned by this entity and a target pin which this entity is attached to


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/geometricpinscomponent)*