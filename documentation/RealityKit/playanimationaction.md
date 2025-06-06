# PlayAnimationAction

**Framework**: RealityKit  
**Kind**: struct

An action that plays an animation on the given target entity with a range of playback options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct PlayAnimationAction
```

#### Overview

Use this action to initiate the playback of animations in a data-driven way. For example, this action can play an animation group which contains a nested action, which plays another animation with specific playback properties.

This action plays the [`AnimationResource`](animationresource.md) from the[`AnimationLibraryComponent`](animationlibrarycomponent.md) on the [`targetEntity`](playanimationaction/targetentity.md). Add all animations to the animation library component that this action will play, ensuring the name of the animation matches the [`animationName`](playanimationaction/animationname.md) being supplied.

[`useParentedControllers`](playanimationaction/useparentedcontrollers.md) is used to determine the playback behavior of the animation this action is playing. Set this to `true` to control the playback of the animation. Calling methods such as [`pause()`](animationplaybackcontroller/pause().md) and [`resume()`](animationplaybackcontroller/resume().md) on the animation playback controller generated from this action will give you control of the animation being played. When the action ends, the animation playback also ends. Set this to `false` to ensure the animation being played runs independently of the action. This would behave as a one shot animation.

The example below is the animation group that the action will play. This contains a sequence containing a single `FromToByAnimation<Transform>`, and character animation.

```swift
// Create an animation group sequence from a range of animations.
let finalAnimation = try AnimationResource
    .group(with: [walkAnimation, moveToAnimation])
```

The example below creates an animation sequence. The final animation in the sequence is an animation generated from the action. This action plays an animation that exist within the [`targetEntity`](playanimationaction/targetentity.md) [`AnimationLibraryComponent`](animationlibrarycomponent.md).

```swift
// An action which plays an animation, with parented controllers.
let playAnimationAction = PlayAnimationAction(animationName: "finalAnimation",
                                              transitionDuration: 0.2,
                                              useParentedControllers: true)

// Creates an animation from the action.
//
// Parented controllers is active. This ensures the action
// plays the entire length of the animation that is being played.
//
// The parameter `finalAnimationDuration` is set to the length
// of the animation group to play.
let finalPlayAnimation = try AnimationResource
    .makeActionAnimation(for: playAnimationAction,
                         duration: finalAnimationDuration)

// Create a sequence of animations that will play. 
//
// The action will play last in the sequence.
let animationSequence = try AnimationResource
    .sequence(with: [idleAnimation, startWalkAnimation, finalPlayAnimation])

// Play the sequence animation that will play the action last.
let animationPlaybackController = entity.playAnimation(animationSequence)
```

> **Note**: If [`useParentedControllers`](playanimationaction/useparentedcontrollers.md) is set to `true`, the animation will play for the duration of the action. Set the duration of the action to match the length of the animation being played to ensure the entire animation plays.

If [`useParentedControllers`](playanimationaction/useparentedcontrollers.md) is set to `true`, the animation will play for the duration of the action. Set the duration of the action to match the length of the animation being played to ensure the entire animation plays.

> ❗ **Important**: This action does not animate a bound property, such as [`BindTarget.transform`](bindtarget/transform.md).

This action does not animate a bound property, such as [`BindTarget.transform`](bindtarget/transform.md).

## Topics

### Initializers
- [init(animationName: String, targetEntity: ActionEntityResolution, transitionDuration: TimeInterval, blendLayer: Int, separateAnimatedValue: Bool, useParentedControllers: Bool, handoffType: AnimationHandoffType)](playanimationaction/init(animationname:targetentity:transitionduration:blendlayer:separateanimatedvalue:useparentedcontrollers:handofftype:).md)
  Creates a new play animation action.
- [init(from: any Decoder) throws](playanimationaction/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var animatedValueType: (any AnimatableData.Type)?](playanimationaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [var animationName: String](playanimationaction/animationname.md)
  The name of the animation resource within the target entity animation library component to start playing.
- [var blendLayer: Int](playanimationaction/blendlayer.md)
  An integer that specifies the order in which to apply animations when more than one animation is playing.
- [var handoffType: AnimationHandoffType](playanimationaction/handofftype.md)
  Type of handoff behavior between a currently-playing animation and the new animation.
- [var separateAnimatedValue: Bool](playanimationaction/separateanimatedvalue.md)
  When set to false, this value indicates that the animation will write directly to the entity’s base value. When set to true, this value indicates that the animation will write to an interim value for the duration of the animation. If this value is set to true then when the animation completes, the entity’s value will be reset to the base value.
- [var targetEntity: ActionEntityResolution](playanimationaction/targetentity.md)
  The entity to play the animation.
- [var transitionDuration: TimeInterval](playanimationaction/transitionduration.md)
  The duration in seconds over which the animation fades in or cross-fades.
- [var useParentedControllers: Bool](playanimationaction/useparentedcontrollers.md)
  A Boolean that indicates whether to parent the new animation’s controller to the controller managing this action.
### Instance Methods
- [func encode(to: any Encoder) throws](playanimationaction/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [PlayAnimationAction.EventParameterType](playanimationaction/eventparametertype.md)
  The associated event parameter type.
### Default Implementations
- [EntityAction Implementations](playanimationaction/entityaction-implementations.md)

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
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.
- [struct SetEntityEnabledAction](setentityenabledaction.md)
  An action that enables or disables the targeted entity and its descendants when played as an animation.
- [struct SpinAction](spinaction.md)
  An action which animates the transform of an entity to rotate around a specified local axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/playanimationaction)*