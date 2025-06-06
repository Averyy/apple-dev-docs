# init(weightNames:frames:name:tweenMode:frameInterval:isAdditive:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Creates an animation that blends between a configuration of blend targets.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(weightNames: [String], frames: [Value], name: String = "", tweenMode: TweenMode = .linear, frameInterval: Float = 1.0 / 30.0, isAdditive: Bool = false, bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1.0)
```

## Parameters

- `weightNames`: The names of the weights in the animated blend shape.
- `frames`: The value of the weights to animate.
- `name`: A textual name for the animation.
- `tweenMode`: An option that determines how animation frames transition.
- `frameInterval`: The duration within the animation timeline for each   frame in the frames array.
- `isAdditive`: A Boolean value that indicates whether the animation   builds on the current state of the target entity or resets the state   before running.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/init(weightnames:frames:name:tweenmode:frameinterval:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*