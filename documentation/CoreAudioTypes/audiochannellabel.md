# AudioChannelLabel

**Framework**: Core Audio Types  
**Kind**: typealias

Identifies how an audio data channel is to be used.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
typealias AudioChannelLabel = UInt32
```

#### Discussion

This data type is used for the `mChannelLabel` field of the [`AudioChannelDescription`](audiochanneldescription.md) structure. See [`Audio Channel Labels`](audio-channel-labels.md) for possible values.

## See Also

- [var mChannelFlags: AudioChannelFlags](audiochanneldescription/mchannelflags.md)
  The audio channel flags that indicate how to interpret the channel coordinates.
- [var mChannelLabel: AudioChannelLabel](audiochanneldescription/mchannellabel.md)
  A label that describes the audio channel.
- [var mCoordinates: (Float32, Float32, Float32)](audiochanneldescription/mcoordinates.md)
  The coordinates that specify a precise speaker location.
- [Audio Channel Coordinates](audio-channel-coordinates.md)
  Used in the `mChannelFlags` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.
- [struct AudioChannelFlags](audiochannelflags.md)
  Constants that define the audio channel flags of an audio channel description.
- [Audio Channel Labels](audio-channel-labels.md)
  Channel labels for use in the `mChannelLabel` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannellabel)*