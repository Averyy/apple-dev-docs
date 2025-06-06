# Entity actions

**Framework**: RealityKit

Create simple, reusable actions that can change your app state, RealityKit scene, or animate an entity.

#### Overview

Entity actions provide an easy way to change or animate parts of your scene, while also allowing you to influence the changes with your app state.

For example, you can vary the size of an impulse you apply to an entity with [`ImpulseAction`](impulseaction.md), play a sound at the end of an entity’s animation with [`PlayAudioAction`](playaudioaction.md), or create a custom action that changes your app state.

## Topics

### Action management
- [protocol EntityAction](entityaction.md)
  A protocol that defines an action for an entity.
- [struct ActionAnimation](actionanimation.md)
  Defines an an action animation.
- [enum ActionEntityResolution](actionentityresolution.md)
  Options available to determine the resolution method for a target entity in an action.
- [protocol ActionHandlerProtocol](actionhandlerprotocol.md)
  The base protocol for action handlers.
### Action events
- [struct ActionEvent](actionevent.md)
  The structure returned to all action event handlers.
- [struct AnimationState](animationstate.md)
  The concretely typed animation state structure.
- [struct ActionEventType](actioneventtype.md)
  A set of events that an action responds to.
- [struct ActionEventDefinition](actioneventdefinition.md)
  Defines an action event interval, and any associated parameters.
- [protocol AnimationStateProtocol](animationstateprotocol.md)
  The protocol representing the current animation state of an action animation.
### Built-in actions
- [struct BillboardAction](billboardaction.md)
  An action that animates the blend factor of an entity’s billboard component.
- [struct EmphasizeAction](emphasizeaction.md)
  An action that performs an animation to call attention to an entity.
- [struct FromToByAction](fromtobyaction.md)
  An action that starts, stops, or increments by a specific value.
- [struct ImpulseAction](impulseaction.md)
  An action that applies an impulse to the physics body at its center of mass when played as an animation.
- [struct OrbitEntityAction](orbitentityaction.md)
  An action which animates the transform of an entity to revolve around a specified pivot entity.
- [struct PlayAnimationAction](playanimationaction.md)
  An action that plays an animation on the given target entity with a range of playback options.
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.
- [struct SetEntityEnabledAction](setentityenabledaction.md)
  An action that enables or disables the targeted entity and its descendants when played as an animation.
- [struct SpinAction](spinaction.md)
  An action which animates the transform of an entity to rotate around a specified local axis.

## See Also

- [Scenes](ecs-scenes.md)
  The context that holds all RealityKit entities.
- [Systems](ecs-systems.md)
  Apply behaviors and physical effects to the entities in a RealityKit scene.
- [Events](ecs-events.md)
  Respond to things happening in your RealityKit scene by subscribing to specific event types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ecs-entity-actions)*