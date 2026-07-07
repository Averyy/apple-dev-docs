# NIDLTDOACoordinatesType.geodetic

**Framework**: Nearby Interaction  
**Kind**: case

A coordinate type that specifies a latitude, longitude, and altitude triplet.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case geodetic
```

#### Discussion

When the coordinate type ([`coordinatesType`](nidltdoameasurement/coordinatestype.md)) for a given measurement ([`NIDLTDOAMeasurement`](nidltdoameasurement.md)) is this option, the value of the measurement’s [`coordinates`](nidltdoameasurement/coordinates.md) is a triplet of the format (latitude, longitude, altitude).

## See Also

- [NIDLTDOACoordinatesType.relative](nidltdoacoordinatestype/relative.md)
  A coordinate type that specifies a 3D Cartesian triplet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoacoordinatestype/geodetic)*