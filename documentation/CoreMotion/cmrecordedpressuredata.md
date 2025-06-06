# CMRecordedPressureData

**Framework**: Core Motion  
**Kind**: class

A recorded measurement of pressure data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- watchOS 5.0+

## Declaration

```swift
class CMRecordedPressureData
```

#### Overview

Use SensorKit’s [`ambientPressure`](https://developer.apple.com/documentation/SensorKit/SRSensor/ambientPressure) sensor to read ambient pressure data.

## Topics

### Instance Properties
- [var identifier: UInt64](cmrecordedpressuredata/identifier.md)
  A value that uniquely identifies this measurement.
- [var startDate: Date](cmrecordedpressuredata/startdate.md)
  The time and date when the system recorded the measurement.

## Relationships

### Inherits From
- [CMAmbientPressureData](cmambientpressuredata.md)
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

- [class CMAmbientPressureData](cmambientpressuredata.md)
  A measurement of the ambient pressure and temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata)*