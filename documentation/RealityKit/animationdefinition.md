# AnimationDefinition

**Framework**: RealityKit  
**Kind**: protocol

The configuration, including target object, timeframe, and visual semantics, of an animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
protocol AnimationDefinition
```

#### Overview

The framework adopts this protocol for several concrete animation objects, such as [`FromToByAnimation`](fromtobyanimation.md), [`SampledAnimation`](sampledanimation.md), [`OrbitAnimation`](orbitanimation.md), [`BlendTreeAnimation`](blendtreeanimation.md), [`AnimationView`](animationview.md), and [`AnimationGroup`](animationgroup.md).

## Topics

### Configuring the animation
- [var name: String](animationdefinition/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](animationdefinition/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](animationdefinition/blendlayer.md)
  The order in which the framework composites the animation.
### Timing the animation
- [var speed: Float](animationdefinition/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationdefinition/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](animationdefinition/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationdefinition/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](animationdefinition/trimduration.md)
  An optional duration that overrides the source animation’s duration.
- [var trimStart: TimeInterval?](animationdefinition/trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](animationdefinition/trimend.md)
  The time, in seconds, at which the source animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](animationdefinition/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.
### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](animationdefinition/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](animationdefinition/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: TimeInterval) -> Self](animationdefinition/repeated(count:)-937w.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](animationdefinition/repeated(count:)-941x8.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](animationdefinition/repeatingforever.md)
  Repeats the animation infinitely.

## Relationships

### Conforming Types
- [ActionAnimation](actionanimation.md)
- [AnimationGroup](animationgroup.md)
- [AnimationView](animationview.md)
- [BlendTreeAnimation](blendtreeanimation.md)
- [FromToByAnimation](fromtobyanimation.md)
- [OrbitAnimation](orbitanimation.md)
- [SampledAnimation](sampledanimation.md)

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
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition)*