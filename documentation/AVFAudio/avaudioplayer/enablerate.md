# enableRate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can adjust the playback rate of the audio player.

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
var enableRate: Bool { get set }
```

```objc
@property BOOL enableRate;
```

## Discussion

To enable modifying the player’s rate, set this property to [`true`](../../Swift/true.md) after you create the player, but before you call [`prepareToPlay()`](./preparetoplay%28%29.md).

## See Also

### Configuring playback settings
- [var volume: Float](./volume.md)
  The audio player’s volume relative to other audio output.
- [func setVolume(Float, fadeDuration: TimeInterval)](./setvolume%28_,fadeduration%29.md)
  Changes the audio player’s volume over a duration of time.
- [var pan: Float](./pan.md)
  The audio player’s stereo pan position.
- [var rate: Float](./rate.md)
  The audio player’s playback rate.
- [var numberOfLoops: Int](./numberofloops.md)
  The number of times the audio repeats playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/enablerate)*