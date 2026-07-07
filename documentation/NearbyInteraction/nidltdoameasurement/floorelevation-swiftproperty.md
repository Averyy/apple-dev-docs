# floorElevation

**Framework**: Nearby Interaction  
**Kind**: property

The floor elevation information for the anchor, if available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@NSCopying
var floorElevation: NIDLTDOAMeasurement.FloorElevation? { get }
```

#### Discussion

This property represents a DL-TDOA anchor’s vertical positioning with support for multi-story buildings. When non-nil, this property contains the floor number and height above the floor where the anchor resides in the physical environment.

## See Also

- [var coordinates: simd_double3](nidltdoameasurement/coordinates.md)
  A triplet that represents the location in 3D space of the anchor that provides the measurement.
- [var coordinatesType: NIDLTDOACoordinatesType](nidltdoameasurement/coordinatestype.md)
  The type of coordinate system that the measurement conforms to.
- [var signalStrength: Double](nidltdoameasurement/signalstrength.md)
  A value that represents the received signal strength, in dBm, from the anchor that provides the measurement.
- [NIDLTDOAMeasurement.FloorElevation](nidltdoameasurement/floorelevation-swift.class.md)
  An object that describes how high off the ground DL-TDOA anchors reside in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/floorelevation-swift.property)*