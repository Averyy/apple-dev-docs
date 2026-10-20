# peakPower(forChannel:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Returns the peak power, in decibels full-scale (dBFS), for an audio channel.

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
func peakPower(forChannel channelNumber: Int) -> Float
```

```objc
- (float) peakPowerForChannel:(NSUInteger) channelNumber;
```

#### Return Value

The audio channel’s current peak power.

#### Discussion

Before asking the player for its peak power value, you must call [`updateMeters()`](../avaudioplayer/updatemeters%28%29.md) to generate the latest data. The returned value ranges from `–160` dBFS, indicating minimum power, to 0 dBFS, indicating maximum power.

## Parameters

- `channelNumber`: The number of the channel that you want the peak power value for.

## See Also

### Managing audio-level metering
- [var isMeteringEnabled: Bool](./ismeteringenabled.md)
  A Boolean value that indicates whether you’ve enabled the recorder to generate audio-level metering data.
- [func updateMeters()](./updatemeters%28%29.md)
  Refreshes the average and peak power values for all channels of an audio recorder.
- [func averagePower(forChannel: Int) -> Float](./averagepower%28forchannel%29.md)
  Returns the average power, in decibels full-scale (dBFS), for an audio channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiorecorder/peakpower(forchannel:))*