# ManipulationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that adds fluid and immersive interactive behaviors and effects.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ManipulationComponent
```

#### Overview

`ManipulationComponent` enables rich interaction on entities in 3D space, including gesture-based movement, and audio feedback. When you apply this to an entity, the system enables intuitive manipulation using hands or input devices like a trackpad.

##### Interaction Features

- : - Single-hand or trackpad gestures allow translation of the entity.
- Rotating the hand changes the orientation of the object.
- Two-hand gestures allow intuitive scaling and rotation.
- The system supports handoff between hands for seamless manipulation.
- : - The system plays audio cues at key interaction moments (e.g., pinch, handoff, release).
- To disable system audio or use custom sounds, set [`audioConfiguration`](manipulationcomponent/audioconfiguration-swift.property.md) to `.none`, and use component events to trigger your own audio responses.
- : - `ManipulationComponent` publishes events through the entity’s `Scene` to notify you of key stages in the interaction lifecycle.
- See [`ManipulationEvents`](manipulationevents.md) for details on available events.

When you add this component to an entity, the system modifies the entity’s transform directly. If you need to apply your own transforms, consider applying them to a  instead, or listening to component events and responding accordingly.

##### Interaction Lifecycle

During a typical interaction, the system transitions through several stages, each stage has a specific event in [`ManipulationEvents`](manipulationevents.md). You can subscribe to these events to implement custom behaviors, audio feedback, analytics, or visual responses:

1. : [`ManipulationEvents.WillBegin`](manipulationevents/willbegin.md)
You can use this to add additional feedback, which lets someone know they have begun manipulating the entity.
2. : [`ManipulationEvents.DidHandOff`](manipulationevents/didhandoff.md)
You can use this to provide visual or auditory confirmation of transfer.
3. : [`ManipulationEvents.DidUpdateTransform`](manipulationevents/didupdatetransform.md)
You can use this to drive effects like trails, dynamic shadows, or visual feedback.
4. : [`ManipulationEvents.WillRelease`](manipulationevents/willrelease.md)
You can use this to run a final visual cue that the person’s manipulation of the entity is about to end.
5. : [`ManipulationEvents.WillEnd`](manipulationevents/willend.md)
You can use this event to remove visual cues to show that neither the person nor the app are actively manipulating the entity’s transform anymore.

## Topics

### Creating a manipulation component
- [init()](manipulationcomponent/init.md)
  Creates a manipulation component.
### Configuring the manipulation
- [static func configureEntity(Entity, hoverEffect: HoverEffectComponent.HoverEffect?, allowedInputTypes: InputTargetComponent.InputType?, collisionShapes: [ShapeResource]?)](manipulationcomponent/configureentity(_:hovereffect:allowedinputtypes:collisionshapes:).md)
  Apply a default configuration to an entity to enable to it for use with manipulation component.
- [var audioConfiguration: ManipulationComponent.AudioConfiguration](manipulationcomponent/audioconfiguration-swift.property.md)
  The audio configuration to apply to the object over the course of the interaction.
- [var dynamics: ManipulationComponent.Dynamics](manipulationcomponent/dynamics-swift.property.md)
  The dynamics controlling the object’s movement and behaviors during the interaction.
- [var releaseBehavior: ManipulationComponent.ReleaseBehavior](manipulationcomponent/releasebehavior-swift.property.md)
  The behavior to apply to the object’s transform when someone releases it.
### Structures
- [ManipulationComponent.AudioConfiguration](manipulationcomponent/audioconfiguration-swift.struct.md)
  A configuration for audio playback during an interaction.
- [ManipulationComponent.Dynamics](manipulationcomponent/dynamics-swift.struct.md)
  Settings that allow customization of the interaction behavior per target.
- [ManipulationComponent.HitTargetComponent](manipulationcomponent/hittargetcomponent.md)
  A component that redirects input to a different entity with a `ManipulationComponent`.
- [ManipulationComponent.InputDevice](manipulationcomponent/inputdevice.md)
  Describes an input device like a hand or a trackpad.
- [ManipulationComponent.ReleaseBehavior](manipulationcomponent/releasebehavior-swift.struct.md)
  A behavior describing the path the object takes when it’s released after an interaction.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [struct InputTargetComponent](inputtargetcomponent.md)
  A component that gives an entity the ability to receive system input.
- [struct GestureComponent](gesturecomponent.md)
- [struct EntityTargetValue](entitytargetvalue.md)
  A value containing an original gesture value along with a targeted entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent)*