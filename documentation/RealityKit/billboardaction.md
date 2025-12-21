# BillboardAction

**Framework**: RealityKit  
**Kind**: struct

An action that animates the blend factor of an entity’s billboard component.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct BillboardAction
```

#### Overview

This action animates the [`blendFactor`](billboardcomponent/blendfactor.md) value of an entity’s [`BillboardComponent`](billboardcomponent.md).

Over its duration, the action updates the `blendFactor` property to `1.0`. If you provide a [`transitionIn`](billboardaction/transitionin.md) configuration, the action interpolates the value of the component’s current value for [`blendFactor`](billboardcomponent/blendfactor.md) towards `1.0`. If you provide a [`transitionOut`](billboardaction/transitionout.md) configuration, the action interpolates the component’s [`blendFactor`](billboardcomponent/blendfactor.md) value from `1.0` to its original value for that component.

The example below creates a three-part animation that:

- Interpolates [`blendFactor`](billboardcomponent/blendfactor.md) from `0.0` to `1.0`
- Pauses for one second
- Interpolates [`blendFactor`](billboardcomponent/blendfactor.md) from `1.0` back to `0.0`

```swift
// Load a robot model from a resource file.
let robotModel = try await ModelEntity(named: "vintage_robot")

// A billboard component for the robot model entity.
var billboardComponent = BillboardComponent()

// Disable the billboard at the beginning by setting its blend factor to zero.
billboardComponent.blendFactor = 0.0

// Add the component to the entity.
await robotModel.components.set(billboardComponent)

// A transition that lasts one second.
let billboardTransition = BillboardAction.Transition(
    duration: 1.0,
    timingFunction: .easeInOut
)

// An action that starts and ends with a one second transition.
let billboardAction = BillboardAction(transitionIn: billboardTransition,
                                      transitionOut: billboardTransition)

// A three second animation that adjusts the blend factor twice.
//
// This animation includes a one second pause between both of the action's
// one second transitions in and out by setting the duration one second
// longer than action's total time.
let billboardAnimation = try AnimationResource
    .makeActionAnimation(for: billboardAction,
                         duration: 3.0,
                         bindTarget: .billboardBlendFactor)

// Play the three second billboard animation that adjusts the blend factor.
robotModel.playAnimation(billboardAnimation)
```

> **Note**: If an entity doesn’t have a [`BillboardComponent`](billboardcomponent.md), the default initializer creates one for you so that it can restore the entity back to a state without the billboard.

> ❗ **Important**: This action directly animates the [`BindTarget.billboardBlendFactor`](bindtarget/billboardblendfactor.md) on the bound entity. Ensure a correct bind target is supplied when creating the animation.

Ensure the action can transition back to a non-billboard state by adding the component to the entity and check the [`blendFactor`](billboardcomponent/blendfactor.md) property has a value that you expect.

## Topics

### Structures
- [BillboardAction.Transition](billboardaction/transition.md)
  The duration and timing of how an action event transitions from one state to another.
### Initializers
- [init(transitionIn: BillboardAction.Transition, transitionOut: BillboardAction.Transition)](billboardaction/init(transitionin:transitionout:).md)
  Creates a new billboard action.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](billboardaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var transitionIn: BillboardAction.Transition](billboardaction/transitionin.md)
  The rate of change at the beginning of the action.
- [var transitionOut: BillboardAction.Transition](billboardaction/transitionout.md)
  The rate of change at the end of the action.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityAction](entityaction.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/billboardaction)*