# AudioChannelCoordinateIndex

**Framework**: Core Audio Types  
**Kind**: enum

Indexes the fields of the `mCoordinates` array in an [`AudioChannelDescription`](audiochanneldescription.md) structure.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum AudioChannelCoordinateIndex
```

## Topics

### Coordinates
- [AudioChannelCoordinateIndex.coordinates_BackFront](audiochannelcoordinateindex/coordinates_backfront.md)
  For rectangular coordinates, negative is back and positive is front. The units are specified by the `mChannelFlags` field.
- [AudioChannelCoordinateIndex.coordinates_DownUp](audiochannelcoordinateindex/coordinates_downup.md)
  For rectangular coordinates, negative is below ground level, `0` is ground level, and positive is above ground level. The units are specified by the `mChannelFlags` field.
- [AudioChannelCoordinateIndex.coordinates_LeftRight](audiochannelcoordinateindex/coordinates_leftright.md)
  For rectangular coordinates, negative is left and positive is right. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.
- [static var coordinates_Azimuth: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_azimuth.md)
  For spherical coordinates, `0` is front center, positive is right, negative is left, and measurements are in degrees.
- [static var coordinates_Distance: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_distance.md)
  For spherical coordinates, distance is radially from the center. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.
- [static var coordinates_Elevation: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_elevation.md)
  For spherical coordinates, `+90` is zenith, `0` is horizontal, `-90` is nadir, and measurements are in degrees.
### Initializers
- [init?(rawValue: UInt32)](audiochannelcoordinateindex/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var coordinates_Azimuth: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_azimuth.md)
  For spherical coordinates, `0` is front center, positive is right, negative is left, and measurements are in degrees.
- [static var coordinates_Distance: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_distance.md)
  For spherical coordinates, distance is radially from the center. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.
- [static var coordinates_Elevation: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_elevation.md)
  For spherical coordinates, `+90` is zenith, `0` is horizontal, `-90` is nadir, and measurements are in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelcoordinateindex)*