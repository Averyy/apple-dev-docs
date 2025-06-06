# averagePower(forChannel:)

**Framework**: AVFAudio  
**Kind**: method

Returns the average power, in decibels full-scale (dBFS), for an audio channel.

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
func averagePower(forChannel channelNumber: Int) -> Float
```

#### Return Value

A floating-point value, in dBFS, that indicates the audio channel’s current average power.

#### Discussion

Before asking the player for its average power value, you must call [`updateMeters()`](avaudioplayer/updatemeters().md) to generate the latest data. The returned value ranges from `–160` dBFS, indicating minimum power, to 0 dBFS, indicating maximum power.

## Parameters

- `channelNumber`: The audio channel with the average power value you want to retrieve. Channel numbers are zero-indexed. A monaural signal, or the left channel of a stereo signal, has channel number  .

## See Also

- [var isMeteringEnabled: Bool](avaudioplayer/ismeteringenabled.md)
  A Boolean value that indicates whether the player is able to generate audio-level metering data.
- [func updateMeters()](avaudioplayer/updatemeters.md)
  Refreshes the average and peak power values for all channels of an audio player.
- [func peakPower(forChannel: Int) -> Float](avaudioplayer/peakpower(forchannel:).md)
  Returns the peak power, in decibels full-scale (dBFS), for an audio channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/averagepower(forchannel:))*