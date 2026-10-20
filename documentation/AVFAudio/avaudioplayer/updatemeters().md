# updateMeters()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Refreshes the average and peak power values for all channels of an audio player.

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
func updateMeters()
```

```objc
- (void) updateMeters;
```

## See Also

### Managing audio-level metering
- [var isMeteringEnabled: Bool](./ismeteringenabled.md)
  A Boolean value that indicates whether the player is able to generate audio-level metering data.
- [func averagePower(forChannel: Int) -> Float](./averagepower%28forchannel%29.md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [func peakPower(forChannel: Int) -> Float](./peakpower%28forchannel%29.md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/updatemeters())*