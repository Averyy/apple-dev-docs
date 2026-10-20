# NIDLTDOACoordinatesType.relative

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Case

A coordinate type that specifies a 3D Cartesian triplet.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case relative
```

```c
NIDLTDOACoordinatesTypeRelative
```

#### Discussion

When the coordinate type ([`coordinatesType`](../nidltdoameasurement/coordinatestype.md)) for a given measurement ([`NIDLTDOAMeasurement`](../nidltdoameasurement.md)) is this option, the value of the measurement’s [`coordinates`](../nidltdoameasurement/coordinates.md) is a triplet of the format (x, y, z).

## See Also

### Identifying a coordinate type
- [NIDLTDOACoordinatesType.geodetic](./geodetic.md)
  A coordinate type that specifies a latitude, longitude, and altitude triplet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoacoordinatestype/relative)*