# CMDeviceMotion.SensorLocation

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

Defines the device’s sensor locations.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SensorLocation
```

```c
enum CMDeviceMotionSensorLocation : NSInteger;
```

## Topics

### Sensor Locations
- [CMDeviceMotion.SensorLocation.default](./sensorlocation-swift.enum/default.md)
  The default sensor location.
- [CMDeviceMotion.SensorLocation.headphoneLeft](./sensorlocation-swift.enum/headphoneleft.md)
  The sensor is in the left headphone.
- [CMDeviceMotion.SensorLocation.headphoneRight](./sensorlocation-swift.enum/headphoneright.md)
  The sensor is in the right headphone.
### Initializers
- [init?(rawValue: Int)](./sensorlocation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Sensor Location
- [var sensorLocation: CMDeviceMotion.SensorLocation](./sensorlocation-swift.property.md)
  The location of the sensors that compute the device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/sensorlocation-swift.enum)*