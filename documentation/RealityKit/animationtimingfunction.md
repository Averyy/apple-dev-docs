# AnimationTimingFunction

**Framework**: RealityKit  
**Kind**: struct

The pacing of an animation transition.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AnimationTimingFunction
```

#### Overview

Use an animation timing function to control the pace of an animation transition when you call one of an entity’s animated move methods, like `Entity/move(to:relativeTo:duration:timingFunction:)-905k`. If you omit a timing function from the call, the method uses the [`default`](animationtimingfunction/default.md) timing function.

## Topics

### Creating timing functions
- [static var `default`: AnimationTimingFunction](animationtimingfunction/default.md)
  A timing function that produces the default curve for the transition.
- [static var easeIn: AnimationTimingFunction](animationtimingfunction/easein.md)
  A timing function that produces a gradual starting transition.
- [static var easeInOut: AnimationTimingFunction](animationtimingfunction/easeinout.md)
  A timing function that produces a gradual starting and ending transition.
- [static var easeOut: AnimationTimingFunction](animationtimingfunction/easeout.md)
  A timing function that produces a gradual ending transition.
- [static var linear: AnimationTimingFunction](animationtimingfunction/linear.md)
  A timing function that produces a linear transition.
- [static func cubicBezier(controlPoint1: SIMD2<Float>, controlPoint2: SIMD2<Float>) -> AnimationTimingFunction](animationtimingfunction/cubicbezier(controlpoint1:controlpoint2:).md)
  Creates a timing function that accelerates and then decelerates towards the target value with the cubic bezier shape specified by two control points.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct SampledAnimation](sampledanimation.md)
  An animation that cycles through a series of frames at a constant interval.
- [enum TweenMode](tweenmode.md)
  Options that determine whether an animation switches between frames gradually or abruptly.
- [struct FromToByAnimation](fromtobyanimation.md)
  An animation that starts, stops, or increments by a specific value.
- [struct AnimationView](animationview.md)
  An animation that represents a variation of another animation.
- [struct OrbitAnimation](orbitanimation.md)
  An animation that revolves an entity around its origin.
- [protocol AnimationDefinition](animationdefinition.md)
  The configuration, including target object, timeframe, and visual semantics, of an animation.
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationtimingfunction)*