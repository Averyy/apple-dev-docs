# AudioChannelFlags

**Framework**: Core Audio Types  
**Kind**: struct

Constants that define the audio channel flags of an audio channel description.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioChannelFlags
```

## Topics

### Flags
- [static var meters: AudioChannelFlags](audiochannelflags/meters.md)
  A flag that indicates that unit values are in meters.
- [static var rectangularCoordinates: AudioChannelFlags](audiochannelflags/rectangularcoordinates.md)
  A flag that indicates the channel uses the speaker position’s cartesian coordinates.
- [static var sphericalCoordinates: AudioChannelFlags](audiochannelflags/sphericalcoordinates.md)
  A flag that indicates the channel uses the speaker position’s spherical coordinates.
### Initializers
- [init(rawValue: UInt32)](audiochannelflags/init(rawvalue:).md)
  Creates a audio channel flags structure with a unsigned integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

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
- [Audio Channel Labels](audio-channel-labels.md)
  Channel labels for use in the `mChannelLabel` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelflags)*