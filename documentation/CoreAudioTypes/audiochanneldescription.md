# AudioChannelDescription

**Framework**: Core Audio Types  
**Kind**: struct

A structure that describes a channel of audio data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioChannelDescription
```

## Topics

### Creating a Channel Description
- [init()](audiochanneldescription/init.md)
  Creates an empty channel description.
- [init(mChannelLabel: AudioChannelLabel, mChannelFlags: AudioChannelFlags, mCoordinates: (Float32, Float32, Float32))](audiochanneldescription/init(mchannellabel:mchannelflags:mcoordinates:).md)
  Creates a channel description with a label, flags, and coordinates.
### Accessing the Data
- [var mChannelFlags: AudioChannelFlags](audiochanneldescription/mchannelflags.md)
  The audio channel flags that indicate how to interpret the channel coordinates.
- [var mChannelLabel: AudioChannelLabel](audiochanneldescription/mchannellabel.md)
  A label that describes the audio channel.
- [var mCoordinates: (Float32, Float32, Float32)](audiochanneldescription/mcoordinates.md)
  The coordinates that specify a precise speaker location.
- [typealias AudioChannelLabel](audiochannellabel.md)
  Identifies how an audio data channel is to be used.
- [Audio Channel Coordinates](audio-channel-coordinates.md)
  Used in the `mChannelFlags` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.
- [struct AudioChannelFlags](audiochannelflags.md)
  Constants that define the audio channel flags of an audio channel description.
- [Audio Channel Labels](audio-channel-labels.md)
  Channel labels for use in the `mChannelLabel` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.
### Operators
- [static func == (AudioChannelDescription, AudioChannelDescription) -> Bool](audiochanneldescription/==(_:_:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioChannelLayout](audiochannellayout.md)
  A structure that specifies a channel layout in a file or in hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochanneldescription)*