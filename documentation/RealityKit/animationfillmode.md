# AnimationFillMode

**Framework**: RealityKit  
**Kind**: struct

Options that determine which animation frames display outside of the normal duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AnimationFillMode
```

#### Overview

This structure enables you to lock an animation at its starting frame for a period of time before beginning. You can also lock an animation to its ending frame for a specified amount of time after it finishes, or both.

An animation applies the fill mode you choose when a range determined by [`trimStart`](animationview/trimstart.md), [`trimEnd`](animationview/trimend.md), or [`trimDuration`](animationview/trimduration.md) exceeds the animation’s underlying duration, which the framework calculates as the frame count (see [`frames`](sampledanimation/frames-2j4nj.md)) multiplied by the [`frameInterval`](sampledanimation/frameinterval.md), multiplied by [`speed`](animationdefinition/speed.md).

For example, if you set the [`trimStart`](animationdefinition/trimstart.md) property for an animation of a hand waving to `-1.0` and [`fillMode`](sampledanimation/fillmode.md) to [`backwards`](animationfillmode/backwards.md) or [`both`](animationfillmode/both.md), the hand displays immediately, freezes at the first animation frame for one second, and then begins to wave.

## Topics

### Choosing a fill mode
- [static let none: AnimationFillMode](animationfillmode/none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let forwards: AnimationFillMode](animationfillmode/forwards.md)
  An option that freezes the last frame of the animation until it stops.
- [static let backwards: AnimationFillMode](animationfillmode/backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [static let both: AnimationFillMode](animationfillmode/both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.
### Creating a fill mode
- [init(rawValue: Int8)](animationfillmode/init(rawvalue:).md)
  Creates a fill mode from its backing data type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode)*