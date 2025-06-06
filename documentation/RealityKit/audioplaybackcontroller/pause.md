# pause()

**Framework**: RealityKit  
**Kind**: method

Pauses playback of the audio resource while maintaining the position in the audio stream.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func pause()
```

#### Discussion

Resume playback of a paused audio resource by calling the [`play()`](audioplaybackcontroller/play().md) method.

## See Also

- [func play()](audioplaybackcontroller/play.md)
  Plays the audio resource.
- [func stop()](audioplaybackcontroller/stop.md)
  Stops playback of the audio resource and discards the location in the audio stream.
- [var isPlaying: Bool](audioplaybackcontroller/isplaying.md)
  A Boolean value that indicates whether playback is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/pause())*