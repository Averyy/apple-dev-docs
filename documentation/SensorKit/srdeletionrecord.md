# SRDeletionRecord

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that describes the reason the framework deletes samples.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRDeletionRecord
```

```objc
@interface SRDeletionRecord : NSObject
```

## Overview

When there are gaps in a recorded sensor’s data, deletion records account for the occasions when the framework deliberately removes the records. A deletion record specifies the time range when records are unavailable (see [`startTime`](./srdeletionrecord/starttime.md) and [`endTime`](./srdeletionrecord/endtime.md)), and the [`reason`](./srdeletionrecord/reason.md) for removal.

To access deletion records for a particular sensor, create a new reader by applying the `sr_sensorForDeletionRecordsFromSensor()` extension of [`NSString`](../Foundation/nsstring.md) to the source sensor.

```swift
let deletionRecordsReader = SRSensorReader(sensor: ambientLightSensor.rawValue.sr_sensorForDeletionRecordsFromSensor())
deletionRecordsReader.delegate = myAmbientLightDeletionRecordsDelegate
```

## Topics

### Accessing the Deletion Reason
- [var reason: SRDeletionReason](./srdeletionrecord/reason.md)
  The reason the framework deletes samples.
- [enum SRDeletionReason](./srdeletionreason.md)
  Reasons that the framework deletes samples.
### Accessing the Deletion Time
- [var startTime: SRAbsoluteTime](./srdeletionrecord/starttime.md)
  The time the framework begins deleting samples.
- [var endTime: SRAbsoluteTime](./srdeletionrecord/endtime.md)
  The time the framework finishes deleting samples.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeletionrecord)*