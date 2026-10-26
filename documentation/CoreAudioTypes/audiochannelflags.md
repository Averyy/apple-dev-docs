# AudioChannelFlags

**Framework**: Core Audio Types  
**Kind**: struct  
**Role**: Structure

Constants that define the audio channel flags of an audio channel description.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioChannelFlags
```

```c
enum AudioChannelFlags : UInt32;
```

## Topics

### Flags
- [static var meters: AudioChannelFlags](./audiochannelflags/meters.md)
  A flag that indicates that unit values are in meters.
- [static var rectangularCoordinates: AudioChannelFlags](./audiochannelflags/rectangularcoordinates.md)
  A flag that indicates the channel uses the speaker position’s cartesian coordinates.
- [static var sphericalCoordinates: AudioChannelFlags](./audiochannelflags/sphericalcoordinates.md)
  A flag that indicates the channel uses the speaker position’s spherical coordinates.
- [kAudioChannelFlags_AllOff](./audiochannelflags/kaudiochannelflags_alloff.md)
  All flags are clear.
### Initializers
- [init(rawValue: UInt32)](./audiochannelflags/init%28rawvalue%29.md)
  Creates a audio channel flags structure with a unsigned integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Accessing the Data
- [var mChannelFlags: AudioChannelFlags](./audiochanneldescription/mchannelflags.md)
  The audio channel flags that indicate how to interpret the channel coordinates.
- [var mChannelLabel: AudioChannelLabel](./audiochanneldescription/mchannellabel.md)
  A label that describes the audio channel.
- [var mCoordinates: (Float32, Float32, Float32)](./audiochanneldescription/mcoordinates.md)
  The coordinates that specify a precise speaker location.
- [typealias AudioChannelLabel](./audiochannellabel.md)
  Identifies how an audio data channel is to be used.
- [Audio Channel Coordinates](./audio-channel-coordinates.md)
  Used in the `mChannelFlags` field of an [`AudioChannelDescription`](./audiochanneldescription.md) structure.
- [Audio Channel Labels](./audio-channel-labels.md)
  Channel labels for use in the `mChannelLabel` field of an [`AudioChannelDescription`](./audiochanneldescription.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelflags)*