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

Use SensorKit’s [`ambientPressure`](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure) sensor to read ambient pressure data.

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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CMAmbientPressureData](cmambientpressuredata.md)
  A measurement of the ambient pressure and temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata)*