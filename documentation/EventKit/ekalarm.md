# EKAlarm

**Framework**: EventKit  
**Kind**: class

A class that represents an alarm.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKAlarm
```

#### Overview

An [`EKAlarm`](ekalarm.md) object represents an alarm in Event Kit. Use the [`init(absoluteDate:)`](ekalarm/init(absolutedate:).md) and [`init(relativeOffset:)`](ekalarm/init(relativeoffset:).md) class methods to create an alarm and use the properties to set information about an alarm. In macOS Mountain Lion, you can specify an action to trigger when the alarm fires via the `emailAddress`, `soundName`, or `url` property.

## Topics

### Creating an Alarm
- [init(absoluteDate: Date)](ekalarm/init(absolutedate:).md)
  Creates and returns an alarm with an absolute date.
- [init(relativeOffset: TimeInterval)](ekalarm/init(relativeoffset:).md)
  Creates and returns an alarm with a relative offset.
### Accessing Alarm Dates
- [var absoluteDate: Date?](ekalarm/absolutedate.md)
  The absolute date for the alarm.
- [var relativeOffset: TimeInterval](ekalarm/relativeoffset.md)
  The offset from the start of an event, at which the alarm fires.
### Setting GeoFence-based Alarms
- [enum EKAlarmProximity](ekalarmproximity.md)
  A value indicating whether an alarm is triggered by entering or exiting a region.
- [var proximity: EKAlarmProximity](ekalarm/proximity.md)
  A value indicating how a location-based alarm is triggered.
- [var structuredLocation: EKStructuredLocation?](ekalarm/structuredlocation.md)
  The location to trigger an alarm.
### Triggering Alarm Actions
- [enum EKAlarmType](ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var type: EKAlarmType](ekalarm/type.md)
  The type of action to trigger when the alarm fires.
- [var emailAddress: String?](ekalarm/emailaddress.md)
  The recipient of an email to send when the alarm triggers.
- [var soundName: String?](ekalarm/soundname.md)
  The name of the sound to play when the alarm triggers.

## Relationships

### Inherits From
- [EKObject](ekobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting an alarm](setting-an-alarm.md)
  Alert users of events and reminders with an alarm.
- [class EKStructuredLocation](ekstructuredlocation.md)
  `A` class that specifies a geofence to activate the alarm of a calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm)*