# play()

**Framework**: RealityKit  
**Kind**: method

Plays the audio resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func play()
```

#### Discussion

The controller plays from the beginning of the resource, or from the point at which it was paused if you previously called the [`pause()`](audioplaybackcontroller/pause().md) method during playback. The controller ignores calls to [`play()`](audioplaybackcontroller/play().md) when audio is already playing.

## See Also

- [func pause()](audioplaybackcontroller/pause.md)
  Pauses playback of the audio resource while maintaining the position in the audio stream.
- [func stop()](audioplaybackcontroller/stop.md)
  Stops playback of the audio resource and discards the location in the audio stream.
- [var isPlaying: Bool](audioplaybackcontroller/isplaying.md)
  A Boolean value that indicates whether playback is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/play())*