# SampledAnimation

**Framework**: RealityKit  
**Kind**: struct

An animation that cycles through a series of frames at a constant interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct SampledAnimation<Value> where Value : AnimatableData
```

#### Overview

To specify the data that the animation samples, set one of the `frames` properties that matches the animated property’s type. For example, set the [`frames`](sampledanimation/frames-2j4nj.md) property to interpolate [`Float`](https://developer.apple.com/documentation/Swift/Float) values.

The following code designates a [`SampledAnimation`](sampledanimation.md) to animate a propery of type [`Float`](https://developer.apple.com/documentation/Swift/Float) by specifying the generic typed syntax. The code queues an array of values: `1.0`, `2.0`, and `3.0`.

```swift
// Define the animation type.
typealias SampledAnimationType = SampledAnimation<Float>

// Define the animated property values.
let frameArray: [Float] = [1.0, 2.0, 3.0]
```

To determine how fast the animation progresses from frame to frame, define this structure’s [`frameInterval`](sampledanimation/frameinterval.md) property. The following code specifies a one-second delay between value changes before initializing the animation object.

```swift
// Define a one-second frame interval.
let interval: TimeInterval = 1

// Create the animation.
let sampleAnim = SampledAnimationType(
    frames: frameArray,
    name: "sampledAnim1",
    frameInterval: interval
    isAdditive: true,
    bindTarget: .transform,
    blendLayer: 100,
    repeatMode: .autoReverse,
    fillMode: .backwards,
    trimStart: 1.0,
    trimEnd: 10.0,
    trimDuration: 9.0,
    offset: 2.0,
    delay: 1.0,
    speed: 2.0
)
```

## Topics

### Creating an animation
- [init(frames: [Value], name: String, tweenMode: TweenMode, frameInterval: Float, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](sampledanimation/init(frames:name:tweenmode:frameinterval:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation with a collection of frames that represent incremental steps in the overall timeline.
- [init(jointNames: [String], frames: [Value], name: String, tweenMode: TweenMode, frameInterval: Float, isAdditive: Bool, isScaleAnimated: Bool, isRotationAnimated: Bool, isTranslationAnimated: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](sampledanimation/init(jointnames:frames:name:tweenmode:frameinterval:isadditive:isscaleanimated:isrotationanimated:istranslationanimated:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation that interpolates between two configurations of the given joints.
### Configuring the animation
- [var name: String](sampledanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](sampledanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](sampledanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var jointNames: [String]](sampledanimation/jointnames.md)
  The names of the joints to animate.
- [var isRotationAnimated: Bool](sampledanimation/isrotationanimated.md)
  A Boolean value that indicates whether the animation observes rotational changes in the entity’s transform.
- [var isScaleAnimated: Bool](sampledanimation/isscaleanimated.md)
  A Boolean value that indicates whether the animation observes changes in the entity’s size.
- [var isTranslationAnimated: Bool](sampledanimation/istranslationanimated.md)
  A Boolean value that indicates whether the animation observes translational changes in the entity’s transform.
- [var additive: Bool](sampledanimation/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
- [var tweenMode: TweenMode](sampledanimation/tweenmode.md)
  An option that determines how animation frames transition.
### Defining frames data
- [var frames: [JointTransforms]](sampledanimation/frames-4eeex.md)
  An array of joint transforms in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var frames: [Transform]](sampledanimation/frames-4qotl.md)
  An array of transforms in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var frames: [Double]](sampledanimation/frames-2hobp.md)
  An array of double-precision values in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [Float]](sampledanimation/frames-2j4nj.md)
  An array of floating-point values in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [simd_quatf]](sampledanimation/frames-2h6tu.md)
  An array of quaternions in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD2<Float>]](sampledanimation/frames-9luwf.md)
  An array of floating-point pairs in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD3<Float>]](sampledanimation/frames-1zxo.md)
  An array of floating-point triplets in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD4<Float>]](sampledanimation/frames-2ywfx.md)
  An array of floating-point quadruples in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
### Timing the animation
- [var frameInterval: Float](sampledanimation/frameinterval.md)
  The duration within the animation timeline for each frame in the frames array.
- [var start: TimeInterval](sampledanimation/start.md)
  An integer multiple of the frame interval at which the animation plays.
- [var end: TimeInterval](sampledanimation/end.md)
  An integer multiple of the frame interval at which the animation stops.
- [var speed: Float](sampledanimation/speed.md)
  A factor that changes the animation’s rate of playback.
- [var delay: TimeInterval](sampledanimation/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](sampledanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](sampledanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](sampledanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](sampledanimation/trimstart.md)
  The optional time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](sampledanimation/trimend.md)
  The optional time, in seconds, at which the animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](sampledanimation/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.
### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](sampledanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](sampledanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: TimeInterval) -> Self](sampledanimation/repeated(count:)-3iijb.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](sampledanimation/repeated(count:)-ltbf.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](sampledanimation/repeatingforever.md)
  Repeats the animation infinitely.
### Initializers
- [init(weightNames: [String], frames: [Value], name: String, tweenMode: TweenMode, frameInterval: Float, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](sampledanimation/init(weightnames:frames:name:tweenmode:frameinterval:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation that blends between a configuration of blend targets.
### Instance Properties
- [var frames: [BlendShapeWeights]](sampledanimation/frames-9jtu9.md)
  An array of weights in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var weightNames: [String]](sampledanimation/weightnames.md)
  The names of the weights to animate.
### Default Implementations
- [AnimationDefinition Implementations](sampledanimation/animationdefinition-implementations.md)

## Relationships

### Conforms To
- [AnimationDefinition](animationdefinition.md)

## See Also

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
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation)*