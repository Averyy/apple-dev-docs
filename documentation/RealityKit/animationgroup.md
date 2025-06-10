# AnimationGroup

**Framework**: RealityKit  
**Kind**: struct

A collection of animations that play simultaneously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AnimationGroup
```

#### Overview

This structure concurrently starts the animations it contains. Use a group to:

- Animate more than one property at once.
- Animate the same property at different times.

##### Animate Multiple Properties Concurrently

For each animatable property your animation needs to control, create a group and add an animation to the array argument of the initializer. The following listing begins coding an animation group that colorizes 3D numbers that count down over a 4-second duration.

```swift
let frames: [Float] = [3.0, 2.0, 1.0, 0.0]
let duration = TimeInterval(frames.count)
let anim1 = FromToByAnimation<Float>(name: "colorize", from: 0.0, to: 1.0,
    duration: duration, bindTarget: .parameter("foo"))
let anim2 = SampledAnimation<Float>(frames: frames, name: "count down",
    frameInterval: duration / frames.count, bindTarget: .parameter("bar"))
let group = AnimationGroup(group: [anim1, anim2], name: "group")
```

##### Create a Sequence for the Same Animation

You can play the same animation at different times by grouping multiple [`AnimationDefinition`](animationdefinition.md) objects that refer to the same animated property. To disperse their playback at runtime, give each definition a unique [`delay`](animationdefinition/delay.md).

> ❗ **Important**: The framework processes animations with a lower [`blendLayer`](animationgroup/blendlayer.md) first, and if the [`blendLayer`](animationgroup/blendlayer.md) matches, in the order in which they appear in the groups array. If two animations on the same property overlap durations at runtime, the one that the framework processes second overwrites the first.

## Topics

### Creating an animation group
- [init(group: [any AnimationDefinition], name: String, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](animationgroup/init(group:name:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates a collection of animations that play simultaneously.
### Configuring the group
- [var group: [any AnimationDefinition]](animationgroup/group.md)
  A collection of animations to run.
- [var name: String](animationgroup/name.md)
  A textual name for the group.
- [var bindTarget: BindTarget](animationgroup/bindtarget.md)
  A textual name that refers to a property on which to run the grouped animations.
- [var blendLayer: Int32](animationgroup/blendlayer.md)
  The order in which the framework composites the animation.
- [var additive: Bool](animationgroup/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
- [var group_: [any AnimationDefinition]?](animationgroup/group_.md)
  An optional collection of animations to run.
### Timing the group
- [var speed: Float](animationgroup/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationgroup/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationgroup/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationgroup/offset.md)
  The time, in seconds, at which the animations begin within the duration.
- [var trimDuration: TimeInterval?](animationgroup/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](animationgroup/trimstart.md)
  The time, in seconds, at which the animations play.
- [var trimEnd: TimeInterval?](animationgroup/trimend.md)
  The time, in seconds, at which the animations stop.
### Repeating group playback
- [var repeatMode: AnimationRepeatMode](animationgroup/repeatmode.md)
  An option that determines how the animations repeat.
- [var fillMode: AnimationFillMode](animationgroup/fillmode.md)
  An option that determines which data displays outside of the normal duration.

## Relationships

### Conforms To
- [AnimationDefinition](animationdefinition.md)

## See Also

- [struct SampledAnimation](sampledanimation.md)
  An animation that cycles through a series of frames at a constant interval.
- [enum TweenMode](tweenmode.md)
  Options that determine whether an animation switches between frames gradually or abruptly.
- [struct FromToByAnimation](fromtobyanimation.md)
  An animation that starts, stops, or increments by a specific value.
- [struct AnimationTimingFunction](animationtimingfunction.md)
  The pacing of an animation transition.
- [struct AnimationView](animationview.md)
  An animation that represents a variation of another animation.
- [struct OrbitAnimation](orbitanimation.md)
  An animation that revolves an entity around its origin.
- [protocol AnimationDefinition](animationdefinition.md)
  The configuration, including target object, timeframe, and visual semantics, of an animation.
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup)*