# SetEntityEnabledAction

**Framework**: RealityKit  
**Kind**: struct

An action that enables or disables the targeted entity and its descendants when played as an animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct SetEntityEnabledAction
```

#### Overview

This action toggles the [`targetEntity`](setentityenabledaction/targetentity.md) [`isEnabled`](entity/isenabled.md) flag. Use the animation generated from this action within an animation group to determine when the entity should be enabled, and visible in the scene.

The example below creates an animation which disables the entity after five seconds. In this example, the target entity starts enabled.

```swift
// Create an action entity resolution.
//
// The animation will be played from the parent entity.
let childEntity: ActionEntityResolution = .entityNamed("childEntity")

// Create an action to disable the entity.
let disableEntityAction = SetEntityEnabledAction(targetEntity: childEntity,
                                                 isEnabled: false)

// Create a small positive duration value.
let duration: TimeInterval = 1 / 30.0

// Create an animation to disable the target entity.
let disableEntityAnimation = try AnimationResource
    .makeActionAnimation(for: disableEntityAction,
                         duration: duration,
                         delay: 5.0)

// Play the sequence animation that plays the actions.
rootEntity.playAnimation(disableEntityAnimation)
```

> **Note**: Animations do not play on entities that are disabled. In order to disable, and enable the target entity, play this action on another entity, such as a root entity, or its parent.

Animations do not play on entities that are disabled. In order to disable, and enable the target entity, play this action on another entity, such as a root entity, or its parent.

> ❗ **Important**: This action does not animate a bound property, such as [`BindTarget.transform`](bindtarget/transform.md).

This action does not animate a bound property, such as [`BindTarget.transform`](bindtarget/transform.md).

> 💡 **Tip**: This action performs instantaneously, consider supplying a small positive duration value when creating the animation.

This action performs instantaneously, consider supplying a small positive duration value when creating the animation.

## Topics

### Initializers
- [init(from: any Decoder) throws](setentityenabledaction/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(targetEntity: ActionEntityResolution, isEnabled: Bool)](setentityenabledaction/init(targetentity:isenabled:).md)
  Creates a new set entity enabled action.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](setentityenabledaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var isEnabled: Bool](setentityenabledaction/isenabled.md)
  A Boolean that you set to enable or disable the entity and its descendants.
- [var targetEntity: ActionEntityResolution](setentityenabledaction/targetentity.md)
  The entity to disable or enable.
### Instance Methods
- [func encode(to: any Encoder) throws](setentityenabledaction/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [SetEntityEnabledAction.EventParameterType](setentityenabledaction/eventparametertype.md)
  The associated event parameter type.
### Default Implementations
- [EntityAction Implementations](setentityenabledaction/entityaction-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityAction](entityaction.md)

## See Also

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
- [struct SpinAction](spinaction.md)
  An action which animates the transform of an entity to rotate around a specified local axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/setentityenabledaction)*