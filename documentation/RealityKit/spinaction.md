# SpinAction

**Framework**: RealityKit  
**Kind**: struct

An action which animates the transform of an entity to rotate around a specified local axis.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct SpinAction
```

#### Overview

This action rotates an entity around itself from a specified [`localAxis`](spinaction/localaxis.md) gradually adjusting its local transform. The [`localAxis`](spinaction/localaxis.md) specifies which cartesian axis around which to rotate in local space. The full spin completes after the action has ended.

The example below creates an animation that spins an entity around the x-axis two times for five seconds with a linear transition.

```swift
// Create an action that performs a spin around the specified local axis
// with a linear transition.
let spinAction = SpinAction(revolutions: 2,
                            localAxis: [1, 0, 0],
                            timingFunction: .linear,
                            isAdditive: false)

// A five second animation that plays an animation causing the entity to
// spin around a specified local axis.
let spinAnimation = try AnimationResource
    .makeActionAnimation(for: spinAction,
                         duration: 5.0,
                         bindTarget: .transform)

// Play the five second spin animation.
entity.playAnimation(spinAnimation)
```

> **Note**: Use the [`localAxis`](spinaction/localaxis.md) to determine whether the entity spins clockwise or counterclockwise.

> ❗ **Important**: This action directly animates the [`BindTarget.transform`](bindtarget/transform.md) on the bound entity. Ensure a correct bind target is supplied when creating the animation.

## Topics

### Initializers
- [init(revolutions: Float, localAxis: SIMD3<Float>, timingFunction: AnimationTimingFunction, isAdditive: Bool)](spinaction/init(revolutions:localaxis:timingfunction:isadditive:).md)
  Creates a new spin action.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](spinaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var isAdditive: Bool](spinaction/isadditive.md)
  A Boolean value that indicates whether the animation system additively blends the action’s output with the base value.
- [var localAxis: SIMD3<Float>](spinaction/localaxis.md)
  A vector that describes the axis of rotation (in local space).
- [var revolutions: Float](spinaction/revolutions.md)
  The number of rotations to complete before stopping.
- [var timingFunction: AnimationTimingFunction](spinaction/timingfunction.md)
  A timing function that controls the progress of the animation.

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
- [struct SetEntityEnabledAction](setentityenabledaction.md)
  An action that enables or disables the targeted entity and its descendants when played as an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spinaction)*