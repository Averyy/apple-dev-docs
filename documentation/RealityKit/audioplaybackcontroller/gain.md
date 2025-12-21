# gain

**Framework**: RealityKit  
**Kind**: property

The individual gain in decibels of the audio playback controller output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var gain: AudioPlaybackController.Decibel { get set }
```

#### Discussion

The gain must be zero or negative, where zero is nominal loudness and negative infinity is silent. If the gain is positive, it will be reset to zero.

Use the [`fade(to:duration:)`](audioplaybackcontroller/fade(to:duration:).md) method to change the gain gradually and create smooth transitions.

## See Also

- [func fade(to: AudioPlaybackController.Decibel, duration: TimeInterval)](audioplaybackcontroller/fade(to:duration:).md)
  Transitions the gain to the given value over a time interval using a linear curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/gain)*