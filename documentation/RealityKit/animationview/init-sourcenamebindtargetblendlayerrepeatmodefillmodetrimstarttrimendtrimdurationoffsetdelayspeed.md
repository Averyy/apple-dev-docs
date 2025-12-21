# init(source:name:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Creates a variation of the given animation by overriding its properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(source: any AnimationDefinition, name: String = "", bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1.0)
```

## Parameters

- `source`: The original animation that this structure modifies.
- `name`: A textual name for the animation.
- `bindTarget`: A textual name that identifies the animated property.
- `blendLayer`: The order in which the framework visually composites the   animation among other running animations.
- `repeatMode`: An option that determines how the animation repeats   outside the length of the view.
- `fillMode`: The behavior when the animated property reaches its end value.
- `trimStart`: The optional time, in seconds, at which the source animation plays.
- `trimEnd`: The optional time, in seconds, at which the source animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that lapses before the animation plays.
- `speed`: A factor that increases or decreases the animation’s playback rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/init(source:name:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*