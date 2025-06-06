# FromToByAction

**Framework**: RealityKit  
**Kind**: struct

An action that starts, stops, or increments by a specific value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct FromToByAction<Value> where Value : AnimatableData
```

#### Overview

This action animates a bound parameters value over time. Specifying a [`from`](fromtobyaction/from.md) value represents the animated properties’ initial value at the start of the animation. Specifying a [`to`](fromtobyaction/to.md) determines the value of the property at the end of the animation. Specifying a[`by`](fromtobyaction/by.md) adds a value to the properties initial state, which calculates the value at the end of the animation.

This action exposes [`FromToByAction.TransformMode`](fromtobyaction/transformmode.md) which is used when animating a [`Transform`](transform.md) property. Use this mode to determine the reference space the property is relative to. For example, [`FromToByAction.TransformMode.local`](fromtobyaction/transformmode/local.md) means the provided transforms are relative to the transform of the bound entity. The only exception is when [`by`](fromtobyaction/by.md) is specified, this is relative to the space of the starting transform.

> **Note**: `FromToByAction` doesn’t support [`JointTransforms`](jointtransforms.md) or [`BlendShapeWeights`](blendshapeweights.md) types. Use [`FromToByAnimation`](fromtobyanimation.md) to animate these types.

`FromToByAction` doesn’t support [`JointTransforms`](jointtransforms.md) or [`BlendShapeWeights`](blendshapeweights.md) types. Use [`FromToByAnimation`](fromtobyanimation.md) to animate these types.

##### Creating a From to By Action to Animate an Entitys Opacity

The example below creates an animation which gradually animates the bound  entity’s opacity property for five seconds with a linear transition. In this example, the entity starts with opacity at `1.0`.

```swift
// Create an action that gradually animates a float value
// towards `0.0`, with a linear transition.
//
// This action does not have a `from` value supplied, 
// meaning this starts from the default source value.
let opacityAction = FromToByAction<Float>(to: 0.0,
                                          timing: .linear,
                                          isAdditive: false)

// A five second animation that plays an animation causing the entity to
// gradually animate the `.opacity` property towards `0.0`.
//
// This makes the entity fade-out.
let opacityAnimation = try AnimationResource
    .makeActionAnimation(for: opacityAction,
                         duration: 5.0,
                         bindTarget: .opacity)

// Play the five second animation on the entity that will fade-out.
entity.playAnimation(opacityAnimation)
```

##### Create a From to By Action to Animate an Entitys Transform Property

The example below creates an animation which gradually animates the bound entities transform property for five seconds with a linear transition.

```swift
// Create a transform to start animating from.
let startTransform = Transform(translation: [0.0, 2.0, 0.0])

// Create a transform to animate towards.
let endTransform = Transform(translation: [0.0, -2.0, 0.0])

// Create an action that gradually animates a transform value.
//
// This starts `from` a specified value, and animates towards
// a specified `to` value.
//
// The bound entity will move in the space relative to its parent.
let transformAction = FromToByAction<Transform>(from: startTransform,
                                                to: endTransform,
                                                mode: .parent,
                                                timing: .linear,
                                                isAdditive: false)

// A five second animation that plays an animation causing 
// the entity to gradually move from a specific start, and end transform
let transformAnimation = try AnimationResource
    .makeActionAnimation(for: transformAction,
                         duration: 5.0,
                         bindTarget: .transform)

// Play the five second animation on the entity that will cause it to move.
entity.playAnimation(transformAnimation)
```

> **Note**: The default source value is the base value of the of animated property. If multiple animations target the property, then the framework observes the output of the previous animation as the subsequent animation’s default source value.

The default source value is the base value of the of animated property. If multiple animations target the property, then the framework observes the output of the previous animation as the subsequent animation’s default source value.

> ❗ **Important**: This action animates various bound properties, for example [`BindTarget.transform`](bindtarget/transform.md) on the bound entity. Ensure a correct bind target is supplied when creating the animation.

This action animates various bound properties, for example [`BindTarget.transform`](bindtarget/transform.md) on the bound entity. Ensure a correct bind target is supplied when creating the animation.

> **Note**: For more information on the combination of inputs this action supports see [`FromToByAnimation`](fromtobyanimation.md).

For more information on the combination of inputs this action supports see [`FromToByAnimation`](fromtobyanimation.md).

> ❗ **Important**: If you do not provide values for any of the `from`, `to`, and `by` parameters, the animation stays at the default source value.

If you do not provide values for any of the `from`, `to`, and `by` parameters, the animation stays at the default source value.

## Topics

### Initializers
- [init(by: Value, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(by:timing:isadditive:).md)
  Creates a new action to animate from the deaultSource by a transform relative to the starting transform.
- [init(from: Value, by: Value?, mode: FromToByAction<Value>.TransformMode, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(from:by:mode:timing:isadditive:).md)
  Creates a new action that interpolates from a specified starting transform towards a specified transform, which is relative to the start. Alternatively, interpolates towards the default source if `by` is not supplied.
- [init(from: Value?, by: Value, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(from:by:timing:isadditive:).md)
  Creates a new action that interpolates towards a specified value, which is relative to the starting value.
- [init(from: Value, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(from:timing:isadditive:).md)
  Creates a new from to by action to animate from a specified value, towards the defaultSource value.
- [init(from: Value?, to: Value, mode: FromToByAction<Value>.TransformMode, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(from:to:mode:timing:isadditive:).md)
  Creates a new action that interpolates towards a specified final transform.
- [init(from: Value?, to: Value, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(from:to:timing:isadditive:).md)
  Creates a new action that interpolates towards a specified final value.
- [init(to: Value, by: Value, mode: FromToByAction<Value>.TransformMode, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(to:by:mode:timing:isadditive:).md)
  Creates a action to animate towards a final value. The starting value is determined by adding the inverse of `by` to the specified final value.
- [init(to: Value, by: Value, timing: AnimationTimingFunction, isAdditive: Bool)](fromtobyaction/init(to:by:timing:isadditive:).md)
  Creates a new from to by action to animate towards a final value. The starting value is determined by adding the inverse of `by` to the specified final value.
### Instance Properties
- [let animatedValueType: (any AnimatableData.Type)?](fromtobyaction/animatedvaluetype.md)
  The type for the value that the action modifies over time.
- [let by: Value?](fromtobyaction/by.md)
  The amount that the animated property changes during the animation.
- [let from: Value?](fromtobyaction/from.md)
  The state of the animated property before the animation starts.
- [var isAdditive: Bool](fromtobyaction/isadditive.md)
  A Boolean value that indicates whether the animation system additively blends the action’s output with the base value.
- [let isReversible: Bool](fromtobyaction/isreversible.md)
  Specifies whether you can play this action in reverse in order to undo prior operations.
- [var mode: FromToByAction<Transform>.TransformMode?](fromtobyaction/mode.md)
  Determines the entities transform [`from`](fromtobyaction/from.md) and [`to`](fromtobyaction/to.md) are relative to.
- [var timingFunction: AnimationTimingFunction](fromtobyaction/timingfunction.md)
  A timing function that controls the progress of the animation.
- [let to: Value?](fromtobyaction/to.md)
  The state of the animated property after the animation ends.
### Type Aliases
- [FromToByAction.EventParameterType](fromtobyaction/eventparametertype.md)
  The associated event parameter type.
### Enumerations
- [FromToByAction.DecodingErrors](fromtobyaction/decodingerrors.md)
- [FromToByAction.TransformMode](fromtobyaction/transformmode.md)
  Options available to determine the space the bound entity should be relative to.
### Default Implementations
- [Decodable Implementations](fromtobyaction/decodable-implementations.md)
- [Encodable Implementations](fromtobyaction/encodable-implementations.md)
- [EntityAction Implementations](fromtobyaction/entityaction-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction)*