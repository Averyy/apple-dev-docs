# isPlaying

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether playback is currently active.

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
@preconcurrency var isPlaying: Bool { get }
```

## Discussion

You may experience a small delay between when you call the [`play()`](./play%28%29.md) method and when the [`isPlaying`](./isplaying.md) property reports `true`.

## See Also

### Starting and stopping audio playback
- [func play()](./play%28%29.md)
  Plays the audio resource.
- [func pause()](./pause%28%29.md)
  Pauses playback of the audio resource while maintaining the position in the audio stream.
- [func stop()](./stop%28%29.md)
  Stops playback of the audio resource and discards the location in the audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/isplaying)*