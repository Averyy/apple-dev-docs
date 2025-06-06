# coordinates_Distance

**Framework**: Core Audio Types  
**Kind**: property

For spherical coordinates, distance is radially from the center. The units are specified by the `mChannelFlags` field of the `AudioChannelDescription` structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var coordinates_Distance: AudioChannelCoordinateIndex { get }
```

## See Also

- [enum AudioChannelCoordinateIndex](audiochannelcoordinateindex.md)
  Indexes the fields of the `mCoordinates` array in an [`AudioChannelDescription`](audiochanneldescription.md) structure.
- [static var coordinates_Azimuth: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_azimuth.md)
  For spherical coordinates, `0` is front center, positive is right, negative is left, and measurements are in degrees.
- [static var coordinates_Elevation: AudioChannelCoordinateIndex](audiochannelcoordinateindex/coordinates_elevation.md)
  For spherical coordinates, `+90` is zenith, `0` is horizontal, `-90` is nadir, and measurements are in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelcoordinateindex/coordinates_distance)*