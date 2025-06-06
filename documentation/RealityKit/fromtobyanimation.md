# FromToByAnimation

**Framework**: RealityKit  
**Kind**: struct

An animation that starts, stops, or increments by a specific value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct FromToByAnimation<Value> where Value : AnimatableData
```

#### Overview

To animate an entity or scene, this structure gradually changes a parameter’s value over time. You can specify a  value, which represents the animated property’s initial value at the beginning of the animation. You can also specify a  value, which determines the value of the property at the end of the animation. Alternatively, you can set a  value. The framework adds the  value to the property’s initial state to calculate the value at the end of the animation.

To specify the property that this struct animates, define `bindTarget` in the intializer,

[`init(name:from:to:by:duration:timing:isAdditive:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)`](fromtobyanimation/init(name:from:to:by:duration:timing:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md).

##### Configure the Animation Inputs

This animation supports varying input combinations, which exhibit the following behavior. When you specify:

The default source value is the base value of the of animated property. If multiple animations target the property, then the framework observes the output of the previous animation as the subsequent animation’s default source value. The default target value is the base value of the animated property.

## Topics

### Creating an animation
- [init(name: String, from: Value?, to: Value?, by: Value?, duration: TimeInterval, timing: AnimationTimingFunction, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](fromtobyanimation/init(name:from:to:by:duration:timing:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation that interpolates between two values for a property of the target entity.
- [init(jointNames: [String], name: String, isScaleAnimated: Bool, isRotationAnimated: Bool, isTranslationAnimated: Bool, from: Value?, to: Value?, by: Value?, duration: TimeInterval, timing: AnimationTimingFunction, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](fromtobyanimation/init(jointnames:name:isscaleanimated:isrotationanimated:istranslationanimated:from:to:by:duration:timing:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation that interpolates between two configurations of the given joints.
### Configuring the animation
- [var name: String](fromtobyanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](fromtobyanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](fromtobyanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var jointNames: [String]](fromtobyanimation/jointnames.md)
  Joint names that define the joints in the skeletal pose.
- [var isScaleAnimated: Bool](fromtobyanimation/isscaleanimated.md)
  A Boolean value that indicates whether that animation interpolates changes to the target’s size.
- [var isRotationAnimated: Bool](fromtobyanimation/isrotationanimated.md)
  A Boolean value that indicates whether the animation interpolates rotational changes.
- [var isTranslationAnimated: Bool](fromtobyanimation/istranslationanimated.md)
  A Boolean value that indicates whether the animation interpolates changes to the target object’s position.
- [var isAdditive: Bool](fromtobyanimation/isadditive.md)
  A Boolean value that indicates whether the animation blends additively with concurrent animations.
### Defining a start value
- [var fromValue: JointTransforms?](fromtobyanimation/fromvalue-2h2wq.md)
- [var fromValue: Transform?](fromtobyanimation/fromvalue-8dr21.md)
- [var fromValue: Double?](fromtobyanimation/fromvalue-4tv25.md)
- [var fromValue: Float?](fromtobyanimation/fromvalue-umpp.md)
- [var fromValue: simd_quatf?](fromtobyanimation/fromvalue-12wzs.md)
- [var fromValue: SIMD2<Float>?](fromtobyanimation/fromvalue-5kx2b.md)
- [var fromValue: SIMD3<Float>?](fromtobyanimation/fromvalue-6msd.md)
- [var fromValue: SIMD4<Float>?](fromtobyanimation/fromvalue-5ckq7.md)
### Defining an incremental value
- [var byValue: JointTransforms?](fromtobyanimation/byvalue-9zcwv.md)
- [var byValue: Transform?](fromtobyanimation/byvalue-5fewc.md)
- [var byValue: Double?](fromtobyanimation/byvalue-3soon.md)
- [var byValue: Float?](fromtobyanimation/byvalue-8na9o.md)
- [var byValue: simd_quatf?](fromtobyanimation/byvalue-460jf.md)
- [var byValue: SIMD2<Float>?](fromtobyanimation/byvalue-1pq4.md)
- [var byValue: SIMD3<Float>?](fromtobyanimation/byvalue-3bp3q.md)
- [var byValue: SIMD4<Float>?](fromtobyanimation/byvalue-7zwq3.md)
### Defining an end value
- [var toValue: JointTransforms?](fromtobyanimation/tovalue-50qb4.md)
- [var toValue: Transform?](fromtobyanimation/tovalue-8jzdy.md)
- [var toValue: Double?](fromtobyanimation/tovalue-4nrhr.md)
- [var toValue: Float?](fromtobyanimation/tovalue-4m4pm.md)
- [var toValue: simd_quatf?](fromtobyanimation/tovalue-4wi6r.md)
- [var toValue: SIMD2<Float>?](fromtobyanimation/tovalue-6a1uy.md)
- [var toValue: SIMD3<Float>?](fromtobyanimation/tovalue-813jk.md)
- [var toValue: SIMD4<Float>?](fromtobyanimation/tovalue-5ki8u.md)
### Timing the animation
- [var speed: Float](fromtobyanimation/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](fromtobyanimation/delay.md)
  An amount of time that elapses before the animation plays.
- [var duration: TimeInterval](fromtobyanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](fromtobyanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var timing: AnimationTimingFunction](fromtobyanimation/timing.md)
  An option that determines the animation’s pace over time.
- [var trimDuration: TimeInterval?](fromtobyanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](fromtobyanimation/trimstart.md)
  The time, in seconds, at which the animation plays.
- [var trimEnd: TimeInterval?](fromtobyanimation/trimend.md)
  The time, in seconds, at which the animation stops.
- [func trimmed(start: TimeInterval?, end: TimeInterval?, duration: TimeInterval?) -> Self](fromtobyanimation/trimmed(start:end:duration:).md)
  Edits the animation duration according to the specified time.
### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](fromtobyanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](fromtobyanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.
- [func repeated(count: TimeInterval) -> Self](fromtobyanimation/repeated(count:)-4f0eh.md)
  Repeats an animation the number of times specified by an irrational number.
- [func repeated(count: Int) -> Self](fromtobyanimation/repeated(count:)-1ykci.md)
  Repeats an animation the number of times specified by a whole number.
- [func repeatingForever() -> Self](fromtobyanimation/repeatingforever.md)
  Repeats the animation infinitely.
### Initializers
- [init(weightNames: [String], name: String, from: Value?, to: Value?, by: Value?, duration: TimeInterval, timing: AnimationTimingFunction, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](fromtobyanimation/init(weightnames:name:from:to:by:duration:timing:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation that blends between a configuration of blend targets.
### Instance Properties
- [var byValue: BlendShapeWeights?](fromtobyanimation/byvalue-2m18u.md)
- [var fromValue: BlendShapeWeights?](fromtobyanimation/fromvalue-66cs6.md)
- [var toValue: BlendShapeWeights?](fromtobyanimation/tovalue-5zgql.md)
- [var weightNames: [String]](fromtobyanimation/weightnames.md)
  Weight names that define the weights for the blend shape.
### Default Implementations
- [AnimationDefinition Implementations](fromtobyanimation/animationdefinition-implementations.md)

## Relationships

### Conforms To
- [AnimationDefinition](animationdefinition.md)

## See Also

- [struct SampledAnimation](sampledanimation.md)
  An animation that cycles through a series of frames at a constant interval.
- [enum TweenMode](tweenmode.md)
  Options that determine whether an animation switches between frames gradually or abruptly.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation)*