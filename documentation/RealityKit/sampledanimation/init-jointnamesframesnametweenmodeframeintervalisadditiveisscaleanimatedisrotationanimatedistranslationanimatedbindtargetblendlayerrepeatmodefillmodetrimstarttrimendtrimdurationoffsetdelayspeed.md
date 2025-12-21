# init(jointNames:frames:name:tweenMode:frameInterval:isAdditive:isScaleAnimated:isRotationAnimated:isTranslationAnimated:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Creates an animation that interpolates between two configurations of the given joints.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(jointNames: [String], frames: [Value], name: String = "", tweenMode: TweenMode = .linear, frameInterval: Float = 1.0 / 30.0, isAdditive: Bool = false, isScaleAnimated: Bool = true, isRotationAnimated: Bool = true, isTranslationAnimated: Bool = true, bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1.0)
```

## Parameters

- `jointNames`: The names of the joints to animate.
- `frames`: The value of the joints to animate.
- `name`: A textual name for the animation.
- `tweenMode`: An option that determines how animation frames transition.
- `frameInterval`: The duration within the animation timeline for each   frame in the frames array.
- `isAdditive`: A Boolean value that indicates whether the animation   builds on the current state of the target entity or resets the state   before running.
- `isScaleAnimated`: A Boolean value that indicates whether the animation   observes changes in the entity’s size.
- `isRotationAnimated`: A Boolean value that indicates whether the   animation observes rotational changes in the entity’s transform.
- `isTranslationAnimated`: A Boolean value that indicates whether the   animation observes translational changes in the entity’s transform.
- `bindTarget`: A textual name that identifies the particular property   that animates.
- `blendLayer`: The order in which the framework composites the animation   into the view.
- `repeatMode`: An option that determines how the animation repeats.
- `fillMode`: The playback behavior outside of the normal duration.
- `trimStart`: The optional time, in seconds, at which the animation plays.
- `trimEnd`: The optional time, in seconds, at which the animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that elapses before the animation plays.
- `speed`: A factor that changes the animation’s rate of playback.

## See Also

- [init(frames: [Value], name: String, tweenMode: TweenMode, frameInterval: Float, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](sampledanimation/init(frames:name:tweenmode:frameinterval:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates an animation with a collection of frames that represent incremental steps in the overall timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/init(jointnames:frames:name:tweenmode:frameinterval:isadditive:isscaleanimated:isrotationanimated:istranslationanimated:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*