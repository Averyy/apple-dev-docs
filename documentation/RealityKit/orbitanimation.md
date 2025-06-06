# OrbitAnimation

**Framework**: RealityKit  
**Kind**: struct

An animation that revolves an entity around its origin.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct OrbitAnimation
```

#### Overview

This class moves an entity in a circular path by gradually adjusting its local transform. The animation sets the entity’s initial position with [`startTransform`](orbitanimation/starttransform.md) and rotates it around the point `(0,` `0,` `0)`. The [`axis`](orbitanimation/axis.md) specifies which cartesian axis around which to rotate. The full orbit completes after [`duration`](orbitanimation/duration.md) lapses.

If the target entity contains child entities, the target entity orbits the children.

##### Revolve an Entity Around Its Origin

The following code creates an animation that orbits an entity around the y-axis 3 times over `6` seconds.

```swift
let yAxis: SIMD3<Float> = [0, 1, 0]
let startingPosition: SIMD3<Float> = [0.25, 0, 0]

let orbit = OrbitAnimation(
    name: "orbit",
    duration: 6,
    axis: yAxis,
    startTransform: Transform(translation: startingPosition),
    spinClockwise: false,
    orientToPath: true,
    rotationCount: 3,
    bindTarget: .transform
)
```

The newly created animation can be trimmed after creation, to last only 4 seconds.

```swift
// Create an animation clip that skips the first two seconds.
let trimmed = orbit.trimmed(start: 2)
```

Use [`generate(with:)`](animationresource/generate(with:).md) to convert `OrbitAnimation` to an [`AnimationResource`](animationresource.md) that can be applied to your entity with [`playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:)`](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:).md).

## Topics

### Creating an animation
- [init(name: String, duration: TimeInterval, axis: SIMD3<Float>, startTransform: Transform, spinClockwise: Bool, orientToPath: Bool, rotationCount: Float, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, isAdditive: Bool, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](orbitanimation/init(name:duration:axis:starttransform:spinclockwise:orienttopath:rotationcount:bindtarget:blendlayer:repeatmode:fillmode:isadditive:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation that revolves an entity around its origin.
### Configuring the animation
- [var startTransform: Transform](orbitanimation/starttransform.md)
  The pose of the orbiting object at the start of the animation.
- [var axis: SIMD3<Float>](orbitanimation/axis.md)
  A 3D vector that points in the direction of the axis around which to rotate.
- [var name: String](orbitanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](orbitanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](orbitanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var rotationCount: Float](orbitanimation/rotationcount.md)
  The number of times to rotate the target entity before stopping.
- [var spinClockwise: Bool](orbitanimation/spinclockwise.md)
  A Boolean value that indicates whether the object orbits the center point in the clockwise direction.
- [var orientToPath: Bool](orbitanimation/orienttopath.md)
  A Boolean value that indicates whether the orbiting object updates its orientation during the animation to orient itself along the rotation path.
- [var additive: Bool](orbitanimation/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
### Timing the animation
- [var speed: Float](orbitanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](orbitanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](orbitanimation/duration.md)
  The elapsed time for one complete rotation.
- [var offset: TimeInterval](orbitanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](orbitanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](orbitanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](orbitanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](orbitanimation/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.
### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](orbitanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](orbitanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: TimeInterval) -> Self](orbitanimation/repeated(count:)-4kqll.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](orbitanimation/repeated(count:)-5i6tq.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](orbitanimation/repeatingforever.md)
  Repeats the animation infinitely.
### Default Implementations
- [AnimationDefinition Implementations](orbitanimation/animationdefinition-implementations.md)

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
- [protocol AnimationDefinition](animationdefinition.md)
  The configuration, including target object, timeframe, and visual semantics, of an animation.
- [struct AnimationFillMode](animationfillmode.md)
  Options that determine which animation frames display outside of the normal duration.
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation)*