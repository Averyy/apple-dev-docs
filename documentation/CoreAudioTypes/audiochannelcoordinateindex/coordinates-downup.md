# AudioChannelCoordinateIndex.coordinates_DownUp

**Framework**: Core Audio Types  
**Kind**: case

For rectangular coordinates, negative is below ground level, `0` is ground level, and positive is above ground level. The units are specified by the `mChannelFlags` field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case coordinates_DownUp
```

## See Also

- [AudioChannelCoordinateIndex.coordinates_BackFront](audiochannelcoordinateindex/coordinates_backfront.md)
  For rectangular coordinates, negative is back and positive is front. The units are specified by the `mChannelFlags` field.
- [AudioChannelCoordinateIndex.coordinates_LeftRight](audiochannelcoordinateindex/coordinates_leftright.md)
  For rectangular coordinates, negative is left and positive is right. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.
- [static var coordinates_Azimuth: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_azimuth.md)
  For spherical coordinates, `0` is front center, positive is right, negative is left, and measurements are in degrees.
- [static var coordinates_Distance: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_distance.md)
  For spherical coordinates, distance is radially from the center. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.
- [static var coordinates_Elevation: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_elevation.md)
  For spherical coordinates, `+90` is zenith, `0` is horizontal, `-90` is nadir, and measurements are in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelcoordinateindex/coordinates_downup)*