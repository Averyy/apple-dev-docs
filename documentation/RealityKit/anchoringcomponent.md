# AnchoringComponent

**Framework**: RealityKit  
**Kind**: struct

A component that anchors virtual content to a real world target.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct AnchoringComponent
```

#### Overview

This component is essential for getting AR features into RealityKit. Use `AnchoringComponent` to anchor virtual content to a real world target by attaching the component to any [`Entity`](entity.md) in your RealityKit scene.

To create an `AnchoringComponent`, you need to specify a [`AnchoringComponent.Target`](anchoringcomponent/target-swift.enum.md). You can also specify the [`AnchoringComponent.TrackingMode`](anchoringcomponent/trackingmode-swift.struct.md) and the [`AnchoringComponent.PhysicsSimulation`](anchoringcomponent/physicssimulation-swift.enum.md) to control how the entity tracks the anchor and how the physics simulates with the entity.

For example, here’s how to create an entity that targets the left hand’s wrist with predicted tracking mode:

```swift
let target = AnchoringComponent.Target.hand(.left, location: .wrist)
let anchoringComponent = AnchoringComponent(target, trackingMode: .predicted)
let entity = Entity()
entity.components.set(anchoringComponent)
```

The entity with `AnchoringComponent` is inactive when created. RealityKit anchors and activates the entity when it finds an anchor that meets the target requirements. You can check the entity’s anchored status using [`isAnchored`](entity/isanchored.md), or you can subscribe to [`SceneEvents.AnchoredStateChanged`](sceneevents/anchoredstatechanged.md) events to receive scene events.

Similarly, RealityKit unanchors the entity if the target disappears or no longer meets the target requirements.

For more information about anchors, see [`ARKit`](https://developer.apple.com/documentation/ARKit).

## Topics

### Creating the anchor component
- [init(AnchoringComponent.Target)](anchoringcomponent/init(_:)-2wng6.md)
  Creates an anchoring component for a given target.
- [init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode)](anchoringcomponent/init(_:trackingmode:).md)
- [init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode, physicsSimulation: AnchoringComponent.PhysicsSimulation)](anchoringcomponent/init(_:trackingmode:physicssimulation:).md)
  Creates an anchoring component for a given target, tracking mode and physics simulation.
- [init(ARAnchor)](anchoringcomponent/init(_:)-5dney.md)
  Creates an anchoring component with the given AR anchor.
### Setting a target
- [let target: AnchoringComponent.Target](anchoringcomponent/target-swift.property.md)
  The real world anchor target to attach the entity to.
### Setting a tracking mode
- [var trackingMode: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.property.md)
  Defines how the `Entity` tracks its target anchor.
### Setting a physics simulation space
- [var physicsSimulation: AnchoringComponent.PhysicsSimulation](anchoringcomponent/physicssimulation-swift.property.md)
  Specifies the physics simulation spece that the entity and its descendants are in.
### Registering a component type
- [static func registerComponent()](anchoringcomponent/registercomponent.md)
  Registers a new component type.
### Comparing anchoring components
- [static func == (AnchoringComponent, AnchoringComponent) -> Bool](anchoringcomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](anchoringcomponent/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Structures
- [AnchoringComponent.ImageAnchoringSource](anchoringcomponent/imageanchoringsource.md)
  Defines the source of object anchoring target based on how it is created.
- [AnchoringComponent.ObjectAnchoringSource](anchoringcomponent/objectanchoringsource.md)
  Defines the source of object anchoring target based on how it is created.
- [AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.struct.md)
  Decides how the `Entity` tracks its target anchor.
### Enumerations
- [AnchoringComponent.PhysicsSimulation](anchoringcomponent/physicssimulation-swift.enum.md)
  Describes the physics simulation space of the entity and its descendants.
- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
### Default Implementations
- [Component Implementations](anchoringcomponent/component-implementations.md)
- [Equatable Implementations](anchoringcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.struct.md)
  Decides how the `Entity` tracks its target anchor.
- [class AnchorEntity](anchorentity.md)
  An anchor that tethers entities to a scene.
- [protocol HasAnchoring](hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent)*