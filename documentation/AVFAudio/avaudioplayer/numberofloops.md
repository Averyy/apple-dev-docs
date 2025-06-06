# numberOfLoops

**Framework**: AVFAudio  
**Kind**: property

The number of times the audio repeats playback.

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
var numberOfLoops: Int { get set }
```

#### Discussion

The default value of `0` results in the sound playing once. Set a positive integer value to specify the number of times to repeat the sound. For example, a value of `1` plays the sound twice: the original sound and one repetition. Set a negative integer value to loop the sound continuously until you call the [`stop()`](avaudioplayer/stop().md) method.

## See Also

- [var volume: Float](avaudioplayer/volume.md)
  The audio player’s volume relative to other audio output.
- [func setVolume(Float, fadeDuration: TimeInterval)](avaudioplayer/setvolume(_:fadeduration:).md)
  Changes the audio player’s volume over a duration of time.
- [var pan: Float](avaudioplayer/pan.md)
  The audio player’s stereo pan position.
- [var enableRate: Bool](avaudioplayer/enablerate.md)
  A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [var rate: Float](avaudioplayer/rate.md)
  The audio player’s playback rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/numberofloops)*