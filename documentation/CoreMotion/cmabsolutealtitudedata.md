# CMAbsoluteAltitudeData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

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

```objc
@interface CMAbsoluteAltitudeData : CMLogItem
```

#### Overview

Absolute altitude is only available on iPhone 12 and later and Apple Watch 6 or SE and later.

## Topics

### Accessing Altitude Data
- [var altitude: Double](./cmabsolutealtitudedata/altitude.md)
  The absolute altitude of the device relative to sea level, measured in meters.
- [var accuracy: Double](./cmabsolutealtitudedata/accuracy.md)
  The estimated uncertainty of the altimeter in meters, based on one standard deviation.
- [var precision: Double](./cmabsolutealtitudedata/precision.md)
  The recommended resolution for the altitude, in meters.

## Relationships

### Inherits From
- [CMLogItem](./cmlogitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Altitude data
- [class CMAltimeter](./cmaltimeter.md)
  An object that initiates the delivery of altitude-related changes.
- [class CMAltitudeData](./cmaltitudedata.md)
  Data for a recorded change in altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata)*