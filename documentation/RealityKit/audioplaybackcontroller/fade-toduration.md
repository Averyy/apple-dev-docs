# fade(to:duration:)

**Framework**: RealityKit  
**Kind**: method

Transitions the gain to the given value over a time interval using a linear curve.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func fade(to newValue: AudioPlaybackController.Decibel, duration: TimeInterval)
```

## Parameters

- `newValue`: The target decibel level.
- `duration`: How long in seconds the fade should last.

## See Also

- [var gain: AudioPlaybackController.Decibel](audioplaybackcontroller/gain.md)
  The individual gain in decibels of the audio playback controller output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/fade(to:duration:))*