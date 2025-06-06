# isMeteringEnabled

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the player is able to generate audio-level metering data.

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
var isMeteringEnabled: Bool { get set }
```

#### Discussion

By default, the player doesn’t generate audio-level metering data. Because metering uses computing resources, enable it only if you intend to use it.

## See Also

- [func updateMeters()](avaudioplayer/updatemeters.md)
  Refreshes the average and peak power values for all channels of an audio player.
- [func averagePower(forChannel: Int) -> Float](avaudioplayer/averagepower(forchannel:).md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [func peakPower(forChannel: Int) -> Float](avaudioplayer/peakpower(forchannel:).md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/ismeteringenabled)*