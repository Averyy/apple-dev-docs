# stop()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Stops playback of the audio resource and discards the location in the audio stream.

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
@preconcurrency func stop()
```

## Discussion

The next time you call [`play()`](./play%28%29.md), playback starts at the beginning of the stream.

## See Also

### Starting and stopping audio playback
- [func play()](./play%28%29.md)
  Plays the audio resource.
- [func pause()](./pause%28%29.md)
  Pauses playback of the audio resource while maintaining the position in the audio stream.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether playback is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/stop())*