# init(for:events:name:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Constructs an action animation that generates events at user defined times.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(for action: ActionType, events: [ActionAnimation<ActionType>.EventDefinitionType], name: String = "", bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1.0)
```

## Parameters

- `action`: The user action.
- `events`: An array of event definitions defining when each action event occurs.
- `name`: The name of the animation.
- `bindTarget`: A textual name that identifies the particular property   that animates.
- `blendLayer`: The order in which the framework composites the animation   into the view.
- `repeatMode`: An option that determines how the animation repeats.
- `fillMode`: The playback behavior outside of the normal duration.
- `trimStart`: The optional time, in seconds, at which the animation plays.
- `trimEnd`: The optional time, in seconds, at which the animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that lapses before the animation plays.
- `speed`: A factor that changes the animation’s rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionanimation/init(for:events:name:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*