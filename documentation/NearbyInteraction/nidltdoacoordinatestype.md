# NIDLTDOACoordinatesType

**Framework**: Nearby Interaction  
**Kind**: enum

The possible coordinate types for Downlink Time-Difference-of-Arrival measurement updates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum NIDLTDOACoordinatesType
```

#### Overview

The [`NIDLTDOAMeasurement`](nidltdoameasurement.md) class [`coordinates`](nidltdoameasurement/coordinates.md) property is of this type.

For more information on Downlink Time-Difference-of-Arrival measurements, see [`NIDLTDOAConfiguration`](nidltdoaconfiguration.md).

## Topics

### Identifying a coordinate type
- [NIDLTDOACoordinatesType.geodetic](nidltdoacoordinatestype/geodetic.md)
  A coordinate type that specifies a latitude, longitude, and altitude triplet.
- [NIDLTDOACoordinatesType.relative](nidltdoacoordinatestype/relative.md)
  A coordinate type that specifies a 3D Cartesian triplet.
### Creating a coordinate type
- [init?(rawValue: Int)](nidltdoacoordinatestype/init(rawvalue:).md)
  Initializes a coordinate type for a Downlink Time-Difference-of-Arrival measurement.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NIDLTDOAMeasurement](nidltdoameasurement.md)
  Information from a Downlink Time-Difference-of-Arrival anchor that you use to derive a range estimate.
- [enum NIDLTDOAMeasurementType](nidltdoameasurementtype.md)
  The possible phases of downlink positioning signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoacoordinatestype)*