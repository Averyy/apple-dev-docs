# Audio Channel Coordinates

**Framework**: Core Audio Types

Used in the `mChannelFlags` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.

## Topics

### Coordinates
- [enum AudioChannelCoordinateIndex](audiochannelcoordinateindex.md)
  Indexes the fields of the `mCoordinates` array in an [`AudioChannelDescription`](audiochanneldescription.md) structure.
- [static var coordinates_Azimuth: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_azimuth.md)
  For spherical coordinates, `0` is front center, positive is right, negative is left, and measurements are in degrees.
- [static var coordinates_Distance: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_distance.md)
  For spherical coordinates, distance is radially from the center. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.
- [static var coordinates_Elevation: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_elevation.md)
  For spherical coordinates, `+90` is zenith, `0` is horizontal, `-90` is nadir, and measurements are in degrees.
### Flags
- [static var rectangularCoordinates: AudioChannelFlags](audiochannelflags/rectangularcoordinates.md)
  A flag that indicates the channel uses the speaker position’s cartesian coordinates.
- [static var sphericalCoordinates: AudioChannelFlags](audiochannelflags/sphericalcoordinates.md)
  A flag that indicates the channel uses the speaker position’s spherical coordinates.
- [static var meters: AudioChannelFlags](audiochannelflags/meters.md)
  A flag that indicates that unit values are in meters.

## See Also

- [var mChannelFlags: AudioChannelFlags](audiochanneldescription/mchannelflags.md)
  The audio channel flags that indicate how to interpret the channel coordinates.
- [var mChannelLabel: AudioChannelLabel](audiochanneldescription/mchannellabel.md)
  A label that describes the audio channel.
- [var mCoordinates: (Float32, Float32, Float32)](audiochanneldescription/mcoordinates.md)
  The coordinates that specify a precise speaker location.
- [typealias AudioChannelLabel](audiochannellabel.md)
  Identifies how an audio data channel is to be used.
- [struct AudioChannelFlags](audiochannelflags.md)
  Constants that define the audio channel flags of an audio channel description.
- [Audio Channel Labels](audio-channel-labels.md)
  Channel labels for use in the `mChannelLabel` field of an [`AudioChannelDescription`](audiochanneldescription.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audio-channel-coordinates)*