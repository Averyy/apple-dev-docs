# AnimationView

**Framework**: RealityKit  
**Kind**: struct

An animation that represents a variation of another animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AnimationView
```

#### Overview

This structure creates a variation of an existing animation by overriding its configuration. The term  in the name signifies that the variation represents a new visual perspective of the existing animation.

##### Create a Clip of an Animation

By supplying a new beginning time ([`trimStart`](animationview/trimstart.md)) and ending time ([`trimEnd`](animationview/trimend.md)), the following code creates a shorter clip of an existing animation. With [`trimStart`](animationview/trimstart.md) set to `1.0` and [`trimEnd`](animationview/trimend.md) at `2.0`, the clip spans a one-second duration.

```swift
// Create or access an existing animation.
let anim1 = FromToByAnimation<Float>(name: "Anim1",
    from: 100.0, to: 200.0, duration: 10.0)

// Use a view to create a clip of the original animation.
let view = AnimationView(source: anim1,
    name: "clip",
    bindTarget: nil,
    blendLayer: 0,
    repeatMode: .autoReverse,
    fillMode: [],
    trimStart: 1.0,
    trimEnd: 2.0,
    trimDuration: nil,
    offset: 0,
    delay: 0,
    speed: 1.0)

// Create an animation resource from the clip.
clipResource = try? AnimationResource.generate(with: view)

// Play the clip.
myModelEntity.playAnimation(clipResource)
```

##### Define a View in Relation to the Animation Source

The source animation’s timing properties define a  on which the [`trimDuration`](animationview/trimduration.md), [`delay`](animationview/delay.md), and [`speed`](animationview/speed.md) properties operate to derive the view. The [`trimDuration`](animationview/trimduration.md) property specifies which animation data the view displays. If [`trimDuration`](animationview/trimduration.md) exceeds the length of the source animation’s timeline, the animation plays according to the characteristics of [`repeatMode`](animationview/repeatmode.md). The [`delay`](animationview/delay.md) property defines a waiting period before the animation begins, and the [`speed`](animationview/speed.md) determines how fast the view plays in relation to the original pace.

## Topics

### Creating an animation view
- [init(source: any AnimationDefinition, name: String, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](animationview/init(source:name:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates a variation of the given animation by overriding its properties.
### Configuring the animation view
- [var source: (any AnimationDefinition)?](animationview/source.md)
  The original animation that this structure modifies.
- [var name: String](animationview/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](animationview/bindtarget.md)
  A textual name that identifies the animated property.
- [var blendLayer: Int32](animationview/blendlayer.md)
  The order in which the framework composites the animation.
### Timing the animation
- [var speed: Float](animationview/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](animationview/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](animationview/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](animationview/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](animationview/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](animationview/trimstart.md)
  The time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](animationview/trimend.md)
  The time, in seconds, at which the source animation stops.
### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](animationview/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](animationview/fillmode.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview)*