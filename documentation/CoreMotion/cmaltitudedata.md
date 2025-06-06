# CMAltitudeData

**Framework**: Core Motion  
**Kind**: class

Data for a recorded change in altitude.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class CMAltitudeData
```

#### Overview

You do not create instances of this class directly. When you want to receive altimeter changes, create an instance of the [`CMAltimeter`](cmaltimeter.md) class and use that object to query for events or to start the delivery of events. The altimeter object creates new instances of this class at appropriate times and delivers them to the handler you specify.

## Topics

### Getting the Altitude Data
- [var relativeAltitude: NSNumber](cmaltitudedata/relativealtitude.md)
  The change in altitude (in meters) since the first reported event.
- [var pressure: NSNumber](cmaltitudedata/pressure.md)
  The recorded pressure, in kilopascals.

## Relationships

### Inherits From
- [CMLogItem](cmlogitem.md)
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

- [class CMAltimeter](cmaltimeter.md)
  An object that initiates the delivery of altitude-related changes.
- [class CMAbsoluteAltitudeData](cmabsolutealtitudedata.md)
  Data that records a change in absolute altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltitudedata)*