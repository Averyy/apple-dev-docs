# coordinates

**Framework**: Nearby Interaction  
**Kind**: property

A triplet that represents the location in 3D space of the anchor that provides the measurement.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var coordinates: simd_double3 { get }
```

#### Discussion

The measurement’s [`coordinatesType`](nidltdoameasurement/coordinatestype.md) determines the manner in which you interpret this property’s value.

## See Also

- [var coordinatesType: NIDLTDOACoordinatesType](nidltdoameasurement/coordinatestype.md)
  The type of coordinate system that the measurement conforms to.
- [var signalStrength: Double](nidltdoameasurement/signalstrength.md)
  A value that represents the received signal strength, in dBm, from the anchor that provides the measurement.
- [var floorElevation: NIDLTDOAMeasurement.FloorElevation?](nidltdoameasurement/floorelevation-swift.property.md)
  The floor elevation information for the anchor, if available.
- [NIDLTDOAMeasurement.FloorElevation](nidltdoameasurement/floorelevation-swift.class.md)
  An object that describes how high off the ground DL-TDOA anchors reside in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/coordinates)*