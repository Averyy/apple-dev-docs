# InputTargetComponent

**Framework**: RealityKit  
**Kind**: struct

A component that gives an entity the ability to receive system input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct InputTargetComponent
```

#### Overview

This component should be added to an entity to inform the system that it should be treated as a target for input handling. It can be customized to require only specific forms of input like direct or indirect interactions. By default the component is configured to handle all forms of input on the system.

The hit testing shape that defines the entity’s interactive entity is defined by the `CollisionComponent`. To configure an entity for input but avoid any sort of physics-related processing, add an `InputTargetComponent` and `CollisionComponent`, but disable the `CollisionComponent` for collision detection, for example:

```None
// Enable the entity for input.
myEntity.components.set(InputTargetComponent())

// Create a collision component with an empty group and mask.
var collision = CollisionComponent(shapes: [.generateSphere(radius: 0.1)])
collision.filter = CollisionFilter(group: [], mask: [])
myEntity.components.set(collision)
```

`InputTargetComponent` behaves hierarchically, so if it is added to an entity that has descendants with `CollisionComponent`s, those shapes will be used for input handling. The `isEnabled` flag can be used to override this behavior by adding the `InputTargetComponent` to a descendant and setting `isEnabled` to false.

`InputTargetComponent`’s `allowedInputTypes` property allows the entity to only receive the provided types of input. This property also propagates down the hierarchy, but if a descendant also has an `InputTargetComponent` defined, its `allowedInputTypes` property overrides the value provided by the ancestor.

## Topics

### Structures
- [InputTargetComponent.InputType](inputtargetcomponent/inputtype.md)
  A type of input that the `InputTargetComponent`’s entity can receive.
### Operators
- [static func == (InputTargetComponent, InputTargetComponent) -> Bool](inputtargetcomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(allowedInputTypes: InputTargetComponent.InputType)](inputtargetcomponent/init(allowedinputtypes:).md)
  Creates a new instance of an `InputTargetComponent` with a set of `allowedInputTypes` that define what kinds of input the component’s entity can receive.
### Instance Properties
- [var allowedInputTypes: InputTargetComponent.InputType](inputtargetcomponent/allowedinputtypes.md)
  The set of input types this component’s entity can receive.
- [var isEnabled: Bool](inputtargetcomponent/isenabled.md)
  Whether the component’s entity is enabled for input.
### Default Implementations
- [Component Implementations](inputtargetcomponent/component-implementations.md)
- [Equatable Implementations](inputtargetcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [struct EntityTargetValue](entitytargetvalue.md)
  A value containing an original gesture value along with a targeted entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/inputtargetcomponent)*