# CMAbsoluteAltitudeData

**Framework**: Core Motion  
**Kind**: class

Data that records a change in absolute altitude.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class CMAbsoluteAltitudeData
```

#### Overview

Absolute altitude is only available on iPhone 12 and later and Apple Watch 6 or SE and later.

## Topics

### Accessing Altitude Data
- [var altitude: Double](cmabsolutealtitudedata/altitude.md)
  The absolute altitude of the device relative to sea level, measured in meters.
- [var accuracy: Double](cmabsolutealtitudedata/accuracy.md)
  The estimated uncertainty of the altimeter in meters, based on one standard deviation.
- [var precision: Double](cmabsolutealtitudedata/precision.md)
  The recommended resolution for the altitude, in meters.

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
- [class CMAltitudeData](cmaltitudedata.md)
  Data for a recorded change in altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata)*