# mCoordinates

**Framework**: Core Audio Types  
**Kind**: property

The coordinates that specify a precise speaker location.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mCoordinates: (Float32, Float32, Float32)
```

#### Discussion

See [`AudioChannelCoordinateIndex`](audiochannelcoordinateindex.md) for the interpretation of the items in the array.

## See Also

- [var mChannelFlags: AudioChannelFlags](audiochanneldescription/mchannelflags.md)
  The audio channel flags that indicate how to interpret the channel coordinates.
- [var mChannelLabel: AudioChannelLabel](audiochanneldescription/mchannellabel.md)
  A label that describes the audio channel.
- [typealias AudioChannelLabel](audiochannellabel.md)
  Identifies how an audio data channel is to be used.
- [Audio Channel Coordinates](audio-channel-coordinates.md)
  Used in the `mChannelFlags` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.
- [struct AudioChannelFlags](audiochannelflags.md)
  Constants that define the audio channel flags of an audio channel description.
- [Audio Channel Labels](audio-channel-labels.md)
  Channel labels for use in the `mChannelLabel` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochanneldescription/mcoordinates)*