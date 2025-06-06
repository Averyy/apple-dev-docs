# EKStructuredLocation

**Framework**: EventKit  
**Kind**: class

`A` class that specifies a geofence to activate the alarm of a calendar item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKStructuredLocation
```

#### Overview

Use [`init(title:)`](ekstructuredlocation/init(title:).md) to create a new structured location, then set it to the [`structuredLocation`](ekalarm/structuredlocation.md) property of an [`EKAlarm`](ekalarm.md) object.

## Topics

### Creating Structured Locations
- [convenience init(title: String)](ekstructuredlocation/init(title:).md)
  Creates a new structured location with the specified title.
- [convenience init(mapItem: MKMapItem)](ekstructuredlocation/init(mapitem:).md)
  Creates a new structured location with the specified map item.
### Accessing Structured Location Properties
- [var title: String?](ekstructuredlocation/title.md)
  The title of the location.
- [var geoLocation: CLLocation?](ekstructuredlocation/geolocation.md)
  The core location.
- [var radius: Double](ekstructuredlocation/radius.md)
  A minimum distance from the core location that would trigger the alarm or reminder.

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
- [class EKAlarm](ekalarm.md)
  A class that represents an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekstructuredlocation)*