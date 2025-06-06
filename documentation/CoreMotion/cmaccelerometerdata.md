# CMAccelerometerData

**Framework**: Core Motion  
**Kind**: class

A data sample from the device’s three accelerometers.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMAccelerometerData
```

#### Overview

An application accesses `CMAccelerometerData` objects through the block handler specified as the last parameter of the [`startAccelerometerUpdates(to:withHandler:)`](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md) method and through the [`accelerometerData`](cmmotionmanager/accelerometerdata.md) property, both declared by the `CMMotionManager` class. The superclass of `CMAccelerometerData`, [`CMLogItem`](cmlogitem.md), defines a [`timestamp`](cmlogitem/timestamp.md) property that records when the acceleration measurement was taken.

## Topics

### Accessing Accelerometer Data
- [var acceleration: CMAcceleration](cmaccelerometerdata/acceleration.md)
  The acceleration measured by the accelerometer.
- [struct CMAcceleration](cmacceleration.md)
  The type of a structure containing 3-axis acceleration values.

## Relationships

### Inherits From
- [CMLogItem](cmlogitem.md)
### Inherited By
- [CMRecordedAccelerometerData](cmrecordedaccelerometerdata.md)
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

## See Also

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)
  Retrieve data from the onboard accelerometers.
- [class CMRecordedAccelerometerData](cmrecordedaccelerometerdata.md)
  A single piece of accelerometer data that was recorded by the device.
- [class CMSensorRecorder](cmsensorrecorder.md)
  An object that gathers and retrieves accelerometer data from a device.
- [class CMSensorDataList](cmsensordatalist.md)
  A list of the accelerometer data recorded by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)*