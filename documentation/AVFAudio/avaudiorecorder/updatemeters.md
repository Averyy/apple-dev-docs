# updateMeters()

**Framework**: AVFAudio  
**Kind**: method

Refreshes the average and peak power values for all channels of an audio recorder.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func updateMeters()
```

#### Discussion

Call this method to update the level meter data before calling [`averagePower(forChannel:)`](avaudiorecorder/averagepower(forchannel:).md) or [`peakPower(forChannel:)`](avaudiorecorder/peakpower(forchannel:).md).

## See Also

- [var isMeteringEnabled: Bool](avaudiorecorder/ismeteringenabled.md)
  A Boolean value that indicates whether you’ve enabled the recorder to generate audio-level metering data.
- [func averagePower(forChannel: Int) -> Float](avaudiorecorder/averagepower(forchannel:).md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [func peakPower(forChannel: Int) -> Float](avaudiorecorder/peakpower(forchannel:).md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/updatemeters())*