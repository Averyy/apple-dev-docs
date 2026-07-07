# coordinatesType

**Framework**: Nearby Interaction  
**Kind**: property

The type of coordinate system that the measurement conforms to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var coordinatesType: NIDLTDOACoordinatesType { get }
```

#### Discussion

Measurements provide coordinates for the anchor that sends the message. Depending on the configuration of the anchor, the coordinates are in one of two formats: [`NIDLTDOACoordinatesType.geodetic`](nidltdoacoordinatestype/geodetic.md) or [`NIDLTDOACoordinatesType.relative`](nidltdoacoordinatestype/relative.md).

The value of this property determines the manner in which your app interprets the value of the anchor’s [`coordinates`](nidltdoameasurement/coordinates.md).

## See Also

- [var coordinates: simd_double3](nidltdoameasurement/coordinates.md)
  A triplet that represents the location in 3D space of the anchor that provides the measurement.
- [var signalStrength: Double](nidltdoameasurement/signalstrength.md)
  A value that represents the received signal strength, in dBm, from the anchor that provides the measurement.
- [var floorElevation: NIDLTDOAMeasurement.FloorElevation?](nidltdoameasurement/floorelevation-swift.property.md)
  The floor elevation information for the anchor, if available.
- [NIDLTDOAMeasurement.FloorElevation](nidltdoameasurement/floorelevation-swift.class.md)
  An object that describes how high off the ground DL-TDOA anchors reside in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/coordinatestype)*