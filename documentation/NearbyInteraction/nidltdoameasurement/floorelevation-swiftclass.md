# NIDLTDOAMeasurement.FloorElevation

**Framework**: Nearby Interaction  
**Kind**: class

An object that describes how high off the ground DL-TDOA anchors reside in the environment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class FloorElevation
```

#### Overview

Floor elevation specifies the vertical position of DL-TDOA anchors. In multi-story deployments, [`floorNumber`](nidltdoameasurement/floorelevation-swift.class/floornumber.md) specifies the floor that the anchor resides on. The  [`height`](nidltdoameasurement/floorelevation-swift.class/height.md) property describes the anchor’s elevation off of the floor, in meters.

Negative [`floorNumber`](nidltdoameasurement/floorelevation-swift.class/floornumber.md) values indicate areas below ground level, for example, a basement or parking level.

## Topics

### Accessing floor elevation components
- [var floorNumber: Int](nidltdoameasurement/floorelevation-swift.class/floornumber.md)
  The floor number on which the anchor resides.
- [var height: Double](nidltdoameasurement/floorelevation-swift.class/height.md)
  The height above the floor in meters.
### Creating a floor elevation
- [init?(coder: NSCoder)](nidltdoameasurement/floorelevation-swift.class/init(coder:).md)
  Initializes a floor elevation from a decoder.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var coordinates: simd_double3](nidltdoameasurement/coordinates.md)
  A triplet that represents the location in 3D space of the anchor that provides the measurement.
- [var coordinatesType: NIDLTDOACoordinatesType](nidltdoameasurement/coordinatestype.md)
  The type of coordinate system that the measurement conforms to.
- [var signalStrength: Double](nidltdoameasurement/signalstrength.md)
  A value that represents the received signal strength, in dBm, from the anchor that provides the measurement.
- [var floorElevation: NIDLTDOAMeasurement.FloorElevation?](nidltdoameasurement/floorelevation-swift.property.md)
  The floor elevation information for the anchor, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/floorelevation-swift.class)*