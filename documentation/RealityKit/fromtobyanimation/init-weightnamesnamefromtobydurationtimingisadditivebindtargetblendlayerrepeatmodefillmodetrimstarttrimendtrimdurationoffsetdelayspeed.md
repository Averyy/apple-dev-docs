# init(weightNames:name:from:to:by:duration:timing:isAdditive:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Creates an animation that blends between a configuration of blend targets.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(weightNames: [String], name: String = "", from: Value? = nil, to: Value? = nil, by: Value? = nil, duration: TimeInterval = 1.0, timing: AnimationTimingFunction = .linear, isAdditive: Bool = false, bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1.0)
```

## Parameters

- `weightNames`: The names of the weights in the animated blend shape.
- `name`: A unique name for the animation.
- `from`: The state of the target object’s weights before the animation starts.
- `to`: The state of the target object’s weights after the animation finishes.
- `by`: An amount that increments the animated weights during the animation.
- `duration`: The total playback time.
- `timing`: An option that determines the animation’s pace over time.
- `isAdditive`: A Boolean value that indicates whether the animation   blends additively with concurrent animations.
- `bindTarget`: A textual name that identifies the particular property that animates.
- `blendLayer`: The order in which the framework composites the animation   into the view.
- `repeatMode`: An option that determines how the animation repeats.
- `fillMode`: The playback behavior outside of the normal duration.
- `trimStart`: The optional time, in seconds, at which the animation plays.
- `trimEnd`: The optional time, in seconds, at which the animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that elapses before the animation plays.
- `speed`: A factor that increases or decreases the animation’s rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyanimation/init(weightnames:name:from:to:by:duration:timing:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*