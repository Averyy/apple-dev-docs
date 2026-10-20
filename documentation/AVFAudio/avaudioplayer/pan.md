# pan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio player’s stereo pan position.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var pan: Float { get set }
```

```objc
@property float pan;
```

#### Discussion

Set this property value to position the audio in the stereo field. Use a value of `-1.0` to indicate full left, `1.0` for full right, and `0.0` for center.

## See Also

### Configuring playback settings
- [var volume: Float](./volume.md)
  The audio player’s volume relative to other audio output.
- [func setVolume(Float, fadeDuration: TimeInterval)](./setvolume%28_,fadeduration%29.md)
  Changes the audio player’s volume over a duration of time.
- [var enableRate: Bool](./enablerate.md)
  A Boolean value that indicates whether you can adjust the playback rate of the audio player.
- [var rate: Float](./rate.md)
  The audio player’s playback rate.
- [var numberOfLoops: Int](./numberofloops.md)
  The number of times the audio repeats playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/pan)*