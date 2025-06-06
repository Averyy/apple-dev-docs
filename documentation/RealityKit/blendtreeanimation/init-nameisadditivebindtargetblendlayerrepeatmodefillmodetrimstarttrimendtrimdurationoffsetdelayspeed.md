# init(_:name:isAdditive:bindTarget:blendLayer:repeatMode:fillMode:trimStart:trimEnd:trimDuration:offset:delay:speed:)

**Framework**: RealityKit  
**Kind**: init

Creates a unique animation from a combination of other animations in the form of a tree.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
init(_ root: any BlendTreeNode, name: String = "", isAdditive: Bool = false, bindTarget: BindTarget? = nil, blendLayer: Int32 = 0, repeatMode: AnimationRepeatMode = .none, fillMode: AnimationFillMode = [], trimStart: TimeInterval? = nil, trimEnd: TimeInterval? = nil, trimDuration: TimeInterval? = nil, offset: TimeInterval = 0, delay: TimeInterval = 0, speed: Float = 1)
```

## Parameters

- `root`: The first node in a tree of animations.
- `name`: A textual name for the animation.
- `isAdditive`: A Boolean value that indicates whether the animation   builds on the current state of the target entity or resets the state   before running.
- `bindTarget`: A textual name that identifies the particular property   that animates.
- `blendLayer`: The order in which the framework composites the animation   into the view.
- `repeatMode`: An option that determines how the animation repeats.
- `fillMode`: The behavior when the animated property reaches its end value.
- `trimStart`: The optional time, in seconds, at which the source animation plays.
- `trimEnd`: The optional time, in seconds, at which the source animation stops.
- `trimDuration`: An optional duration that overrides the calculated duration.
- `offset`: The time, in seconds, at which the animation begins within the duration.
- `delay`: An amount of time that lapses before the animation plays.
- `speed`: A factor that increases or decreases the animation’s rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/init(_:name:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:))*