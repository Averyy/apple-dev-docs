# gain

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The individual gain in decibels of the audio playback controller output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var gain: AudioPlaybackController.Decibel { get set }
```

## Discussion

The gain must be zero or negative, where zero is nominal loudness and negative infinity is silent. If the gain is positive, it will be reset to zero.

Use the [`fade(to:duration:)`](./fade%28to,duration%29.md) method to change the gain gradually and create smooth transitions.

## See Also

### Setting the volume
- [func fade(to: AudioPlaybackController.Decibel, duration: TimeInterval)](./fade%28to,duration%29.md)
  Transitions the gain to the given value over a time interval using a linear curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/gain)*