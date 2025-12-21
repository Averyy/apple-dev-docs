# isPlaying

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether playback is currently active.

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
@preconcurrency var isPlaying: Bool { get }
```

#### Discussion

You may experience a small delay between when you call the [`play()`](audioplaybackcontroller/play().md) method and when the [`isPlaying`](audioplaybackcontroller/isplaying.md) property reports `true`.

## See Also

- [func play()](audioplaybackcontroller/play.md)
  Plays the audio resource.
- [func pause()](audioplaybackcontroller/pause.md)
  Pauses playback of the audio resource while maintaining the position in the audio stream.
- [func stop()](audioplaybackcontroller/stop.md)
  Stops playback of the audio resource and discards the location in the audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/isplaying)*