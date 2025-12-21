# AttachedTransformComponent

**Framework**: RealityKit  
**Kind**: struct

A component that stores an optional source pin owned by this entity and a target pin which this entity is attached to

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AttachedTransformComponent
```

#### Overview

Attach an entity to a target pin owned by another entity with an optional source pin

## Topics

### Initializers
- [init(source: GeometricPin?, target: GeometricPin)](attachedtransformcomponent/init(source:target:).md)
  Creates an AttachedTransformComponent with an optional source pin and a target pin
### Instance Properties
- [var source: GeometricPin?](attachedtransformcomponent/source.md)
  Optional source pin with an offset relative to the current entity
- [var target: GeometricPin](attachedtransformcomponent/target.md)
  Target pin with an offset relative to the target entity

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Simulating physics joints in your RealityKit app](simulating-physics-joints-in-your-realitykit-app.md)
  Create realistic, connected motion using physics joints.
- [struct GeometricPin](geometricpin.md)
  A structure that identifies a local transform relative to an entity or entity’s animating skeletal joint.
- [struct GeometricPinsComponent](geometricpinscomponent.md)
  A component that stores a sequence of geometric pins.
- [protocol PhysicsJoint](physicsjoint.md)
  A type that describes physics joints.
- [struct PhysicsJointsComponent](physicsjointscomponent.md)
  A component that stores physics joints which RealityKit simulates.
- [struct EntityGeometricPins](entitygeometricpins.md)
  A structure that wraps all geometric pins an entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachedtransformcomponent)*