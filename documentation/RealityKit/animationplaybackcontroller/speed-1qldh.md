# speed

**Framework**: RealityKit  
**Kind**: property

The animation’s rate of playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var speed: Float { get set }
```

#### Discussion

The animation applies the value of this property as an irrational factor of the unaltered speed. For example, a value of `2` plays the animation twice as fast, a value of `0.5` plays the animation at half speed, and a value of `1` plays the animation at the unaltered rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/speed-1qldh)*