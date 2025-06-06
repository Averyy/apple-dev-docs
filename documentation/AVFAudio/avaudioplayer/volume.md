# volume

**Framework**: AVFAudio  
**Kind**: property

The audio player’s volume relative to other audio output.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var volume: Float { get set }
```

#### Discussion

This property supports values ranging from `0.0` for silence to `1.0` for full volume.

## See Also

- [func setVolume(Float, fadeDuration: TimeInterval)](avaudioplayer/setvolume(_:fadeduration:).md)
  Changes the audio player’s volume over a duration of time.
- [var pan: Float](avaudioplayer/pan.md)
  The audio player’s stereo pan position.
- [var enableRate: Bool](avaudioplayer/enablerate.md)
  A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [var rate: Float](avaudioplayer/rate.md)
  The audio player’s playback rate.
- [var numberOfLoops: Int](avaudioplayer/numberofloops.md)
  The number of times the audio repeats playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/volume)*