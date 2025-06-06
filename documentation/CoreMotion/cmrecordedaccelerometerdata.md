# CMRecordedAccelerometerData

**Framework**: Core Motion  
**Kind**: class

A single piece of accelerometer data that was recorded by the device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMRecordedAccelerometerData
```

#### Overview

You do not create instances of this class directly. Instead, you use a [`CMSensorRecorder`](cmsensorrecorder.md) object to retrieve already recorded data from the system.

## Topics

### Getting the Accelerometer Data
- [var startDate: Date](cmrecordedaccelerometerdata/startdate.md)
  The wall clock time when the sensor sample was recorded.
- [var identifier: UInt64](cmrecordedaccelerometerdata/identifier.md)
  The unique identifier for the accelerometer data.

## Relationships

### Inherits From
- [CMAccelerometerData](cmaccelerometerdata.md)
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
- [class CMAccelerometerData](cmaccelerometerdata.md)
  A data sample from the device’s three accelerometers.
- [class CMSensorRecorder](cmsensorrecorder.md)
  An object that gathers and retrieves accelerometer data from a device.
- [class CMSensorDataList](cmsensordatalist.md)
  A list of the accelerometer data recorded by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)*