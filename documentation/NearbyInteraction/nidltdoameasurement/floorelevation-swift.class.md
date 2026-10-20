# NIDLTDOAMeasurement.FloorElevation

**Framework**: Nearby Interaction  
**Kind**: class  
**Role**: Class

An object that describes how high off the ground DL-TDOA anchors reside in the environment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class FloorElevation
```

```objc
@interface NIDLTDOAMeasurementFloorElevation : NSObject
```

#### Overview

Floor elevation specifies the vertical position of DL-TDOA anchors. In multi-story deployments, [`floorNumber`](./floorelevation-swift.class/floornumber.md) specifies the floor that the anchor resides on. The  [`height`](./floorelevation-swift.class/height.md) property describes the anchor’s elevation off of the floor, in meters.

Negative [`floorNumber`](./floorelevation-swift.class/floornumber.md) values indicate areas below ground level, for example, a basement or parking level.

## Topics

### Accessing floor elevation components
- [var floorNumber: Int](./floorelevation-swift.class/floornumber.md)
  The floor number on which the anchor resides.
- [var height: Double](./floorelevation-swift.class/height.md)
  The height above the floor in meters.
### Creating a floor elevation
- [init?(coder: NSCoder)](./init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Locating the anchor
- [var coordinates: simd_double3](./coordinates.md)
  A triplet that represents the location in 3D space of the anchor that provides the measurement.
- [var coordinatesType: NIDLTDOACoordinatesType](./coordinatestype.md)
  The type of coordinate system that the measurement conforms to.
- [var signalStrength: Double](./signalstrength.md)
  A value that represents the received signal strength, in dBm, from the anchor that provides the measurement.
- [var floorElevation: NIDLTDOAMeasurement.FloorElevation?](./floorelevation-swift.property.md)
  The floor elevation information for the anchor, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/floorelevation-swift.class)*