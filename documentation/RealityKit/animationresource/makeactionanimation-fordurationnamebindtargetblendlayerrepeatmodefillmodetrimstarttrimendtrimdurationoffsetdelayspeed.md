# makeActionAnimation(for:duration:name:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: method

Creates an action animation containing a single event definition from an action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func makeActionAnimation<T>(for action: T, duration: TimeInterval = 1.0, name: String = "", bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1.0) throws -> AnimationResource where T : EntityAction
```

#### Return Value

An animation resource to play the given action.

#### Discussion

> **Note**: Duration is clamped to a positive, small non zero value, if duration is zero or less.

## Parameters

- `action`: The user action.
- `duration`: The event interval’s duration.
- `name`: A textual name for the animation.
- `bindTarget`: A textual name that identifies the particular property that animates.
- `blendLayer`: An integer that specifies the order in which to apply animations when more than one animation is playing.
- `repeatMode`: An option that determines how the animation repeats.
- `fillMode`: An option that determines how the animation repeats.
- `trimStart`: The optional time, in seconds, at which the animation plays.
- `trimEnd`: The optional time, in seconds, at which the animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that lapses before the animation plays.
- `speed`: A factor that changes the animation’s rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/makeactionanimation(for:duration:name:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*