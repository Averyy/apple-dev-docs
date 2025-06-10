# ImpulseAction

**Framework**: RealityKit  
**Kind**: struct

An action that applies an impulse to the physics body at its center of mass when played as an animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct ImpulseAction
```

#### Overview

This action requires a [`CollisionComponent`](collisioncomponent.md) and [`PhysicsBodyComponent`](physicsbodycomponent.md) with the [`mode`](physicsbodycomponent/mode.md) set to [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md). Without these settings, the impulse has no effect on the entity.

The example below creates an animation which applies an impulse to the entity after five seconds.

```swift
// Create an action to apply an impulse, forcing the object to move upwards.
let impulseAction = ImpulseAction(linearImpulse: [0, 1, 0])

// Create a small positive duration value.
let duration: TimeInterval = 1 / 30.0

// Create an animation for the action, which will start playing
// after five seconds.
let impulseAnimation = try AnimationResource
    .makeActionAnimation(for: impulseAction,
                         duration: duration,
                         delay: 5.0)

// Play the sequence animation that will play the actions.
entity.playAnimation(impulseAnimation)
```

> ❗ **Important**: This action does not directly animate a bound property, such as [`BindTarget.transform`](bindtarget/transform.md).

> 💡 **Tip**: This action performs instantaneously, consider supplying a small positive duration value when creating the animation.

## Topics

### Initializers
- [init(targetEntity: ActionEntityResolution, linearImpulse: SIMD3<Float>)](impulseaction/init(targetentity:linearimpulse:).md)
  Creates a new impulse action.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](impulseaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var linearImpulse: SIMD3<Float>](impulseaction/linearimpulse.md)
  An impulse in newton seconds (in physics simulation space).
- [var targetEntity: ActionEntityResolution](impulseaction/targetentity.md)
  The entity that the impulse acts upon.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/impulseaction)*