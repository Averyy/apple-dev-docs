# NIDLTDOACoordinatesType.relative

**Framework**: Nearby Interaction  
**Kind**: case

A coordinate type that specifies a 3D Cartesian triplet.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case relative
```

#### Discussion

When the coordinate type ([`coordinatesType`](nidltdoameasurement/coordinatestype.md)) for a given measurement ([`NIDLTDOAMeasurement`](nidltdoameasurement.md)) is this option, the value of the measurement’s [`coordinates`](nidltdoameasurement/coordinates.md) is a triplet of the format (x, y, z).

## See Also

- [NIDLTDOACoordinatesType.geodetic](nidltdoacoordinatestype/geodetic.md)
  A coordinate type that specifies a latitude, longitude, and altitude triplet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoacoordinatestype/relative)*