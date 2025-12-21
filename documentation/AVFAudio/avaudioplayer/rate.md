# rate

**Framework**: AVFAudio  
**Kind**: property

The audio player’s playback rate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rate: Float { get set }
```

#### Discussion

To set an audio player’s playback rate, you must first enable the rate adjustment by setting its [`enableRate`](avaudioplayer/enablerate.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

The default value of this property is `1.0`, which indicates that audio playback occurs at standard speed. This property supports values in the range of `0.5` for half-speed playback to `2.0` for double-speed playback.

> **Note**:  Adjusting the audio’s playback rate doesn’t alter its pitch.

## See Also

- [var volume: Float](avaudioplayer/volume.md)
  The audio player’s volume relative to other audio output.
- [func setVolume(Float, fadeDuration: TimeInterval)](avaudioplayer/setvolume(_:fadeduration:).md)
  Changes the audio player’s volume over a duration of time.
- [var pan: Float](avaudioplayer/pan.md)
  The audio player’s stereo pan position.
- [var enableRate: Bool](avaudioplayer/enablerate.md)
  A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [var numberOfLoops: Int](avaudioplayer/numberofloops.md)
  The number of times the audio repeats playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/rate)*