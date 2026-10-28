# pause()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Pauses playback of the audio resource while maintaining the position in the audio stream.

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
@preconcurrency func pause()
```

## Discussion

Resume playback of a paused audio resource by calling the [`play()`](./play%28%29.md) method.

## See Also

### Starting and stopping audio playback
- [func play()](./play%28%29.md)
  Plays the audio resource.
- [func stop()](./stop%28%29.md)
  Stops playback of the audio resource and discards the location in the audio stream.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether playback is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/pause())*