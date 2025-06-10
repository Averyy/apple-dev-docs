# AnimationHandoffType

**Framework**: RealityKit  
**Kind**: struct

The type of handoff the play animation method performs between a current animation and a new animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct AnimationHandoffType
```

## Topics

### Type Properties
- [static var compose: AnimationHandoffType](animationhandofftype/compose.md)
  Adds the new animation to existing animations, and immediately starts the new animation.
- [static var `default`: AnimationHandoffType](animationhandofftype/default.md)
  Provides the default behavior.
- [static var stop: AnimationHandoffType](animationhandofftype/stop.md)
  Stops the specified animation.
### Type Methods
- [static func replace(applyToAllLayers: Bool) -> AnimationHandoffType](animationhandofftype/replace(applytoalllayers:).md)
  Keeps playing the current animation during the transition time and uses the value from that animation as the blend value for the transition to the new animation.
- [static func snapshotAndReplace(applyToAllLayers: Bool) -> AnimationHandoffType](animationhandofftype/snapshotandreplace(applytoalllayers:).md)
  Stops the current animation and uses the current value of that animation as the blend value for the transition to the new animation.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

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
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationhandofftype)*