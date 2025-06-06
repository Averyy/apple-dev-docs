# setVolume(_:fadeDuration:)

**Framework**: AVFAudio  
**Kind**: method

Changes the audio player’s volume over a duration of time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func setVolume(_ volume: Float, fadeDuration duration: TimeInterval)
```

## Parameters

- `volume`: The target volume.
- `duration`: The duration, in seconds, over which to fade the volume.

## See Also

- [var volume: Float](avaudioplayer/volume.md)
  The audio player’s volume relative to other audio output.
- [var pan: Float](avaudioplayer/pan.md)
  The audio player’s stereo pan position.
- [var enableRate: Bool](avaudioplayer/enablerate.md)
  A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [var rate: Float](avaudioplayer/rate.md)
  The audio player’s playback rate.
- [var numberOfLoops: Int](avaudioplayer/numberofloops.md)
  The number of times the audio repeats playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/setvolume(_:fadeduration:))*