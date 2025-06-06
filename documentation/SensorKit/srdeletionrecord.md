# SRDeletionRecord

**Framework**: SensorKit  
**Kind**: class

An object that describes the reason the framework deletes samples.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRDeletionRecord
```

#### Overview

When there are gaps in a recorded sensor’s data, deletion records account for the occasions when the framework deliberately removes the records. A deletion record specifies the time range when records are unavailable (see [`startTime`](srdeletionrecord/starttime.md) and [`endTime`](srdeletionrecord/endtime.md)), and the [`reason`](srdeletionrecord/reason.md) for removal.

To access deletion records for a particular sensor, create a new reader by applying the `sr_sensorForDeletionRecordsFromSensor()` extension of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) to the source sensor.

```swift
let deletionRecordsReader = SRSensorReader(sensor: ambientLightSensor.rawValue.sr_sensorForDeletionRecordsFromSensor())
deletionRecordsReader.delegate = myAmbientLightDeletionRecordsDelegate
```

## Topics

### Accessing the Deletion Reason
- [var reason: SRDeletionReason](srdeletionrecord/reason.md)
  The reason the framework deletes samples.
- [enum SRDeletionReason](srdeletionreason.md)
  Reasons that the framework deletes samples.
### Accessing the Deletion Time
- [var startTime: SRAbsoluteTime](srdeletionrecord/starttime.md)
  The time the framework begins deleting samples.
- [var endTime: SRAbsoluteTime](srdeletionrecord/endtime.md)
  The time the framework finishes deleting samples.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeletionrecord)*