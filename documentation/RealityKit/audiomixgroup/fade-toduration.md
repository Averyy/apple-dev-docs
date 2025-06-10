# fade(to:duration:)

**Framework**: RealityKit  
**Kind**: method

Transitions the gain to a value over a time interval using a linear curve.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
mutating func fade(to gain: Audio.Decibel, duration: TimeInterval)
```

## Parameters

- `gain`: The overall level for audio from a group after the fade is complete.
- `duration`: The duration of the fade in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiomixgroup/fade(to:duration:))*