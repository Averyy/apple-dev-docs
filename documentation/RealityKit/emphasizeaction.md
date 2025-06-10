# EmphasizeAction

**Framework**: RealityKit  
**Kind**: struct

An action that performs an animation to call attention to an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct EmphasizeAction
```

#### Overview

This action plays a preexisting animation, dependent on the [`style`](emphasizeaction/style.md) and [`motionType`](emphasizeaction/motiontype.md) options.

The example below creates an animation that causes the entity to bounce in a playful style.

```swift
// An action that performs a bounce motion in a playful style.
let emphasizeAction = EmphasizeAction(motionType: .bounce,
                                      style: .playful,
                                      isAdditive: false)

// A five second animation that plays the preexisting animation.
//
// This animation causes the entity to raise up, and then drop,
// appearing to bounce on the ground in a playful style,
// before returning to its original position.
let playfulBounceAnimation = try AnimationResource
    .makeActionAnimation(for: emphasizeAction,
                         duration: 5.0,
                         bindTarget: .transform)

// Play the five second emphasize animation that causes the entity to
// bounce in a playful style.
entity.playAnimation(playfulBounceAnimation)
```

> ❗ **Important**: This action directly animates the [`BindTarget.transform`](bindtarget/transform.md) on the bound entity. Ensure a correct bind target is supplied when creating the animation.

## Topics

### Initializers
- [init(motionType: EmphasizeAction.EmphasisMotionType, style: EmphasizeAction.EmphasisAnimationStyle, isAdditive: Bool)](emphasizeaction/init(motiontype:style:isadditive:).md)
  Creates a new emphasize action.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](emphasizeaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var isAdditive: Bool](emphasizeaction/isadditive.md)
  A Boolean value that indicates whether the animation system additively blends the action’s output with the base value.
- [var motionType: EmphasizeAction.EmphasisMotionType](emphasizeaction/motiontype.md)
  An option that implements animation effects.
- [var style: EmphasizeAction.EmphasisAnimationStyle](emphasizeaction/style.md)
  An option that implements different kinds of animation timing.
### Enumerations
- [EmphasizeAction.EmphasisAnimationStyle](emphasizeaction/emphasisanimationstyle.md)
  Options available to determine the kinds of animation timing.
- [EmphasizeAction.EmphasisMotionType](emphasizeaction/emphasismotiontype.md)
  Options available to determine the kinds of animation effects.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityAction](entityaction.md)

## See Also

- [struct BillboardAction](billboardaction.md)
  An action that animates the blend factor of an entity’s billboard component.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/emphasizeaction)*