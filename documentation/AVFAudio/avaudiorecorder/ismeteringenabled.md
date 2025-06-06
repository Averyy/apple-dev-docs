# isMeteringEnabled

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether you’ve enabled the recorder to generate audio-level metering data.

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
var isMeteringEnabled: Bool { get set }
```

#### Discussion

By default, the recorder doesn’t generate audio-level metering data. Because metering uses computing resources, enable it only if you intend to use it.

## See Also

- [func updateMeters()](avaudiorecorder/updatemeters.md)
  Refreshes the average and peak power values for all channels of an audio recorder.
- [func averagePower(forChannel: Int) -> Float](avaudiorecorder/averagepower(forchannel:).md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.
- [func peakPower(forChannel: Int) -> Float](avaudiorecorder/peakpower(forchannel:).md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/ismeteringenabled)*