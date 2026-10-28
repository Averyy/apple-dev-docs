# CMRecordedPressureData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

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

```objc
@interface CMRecordedPressureData : CMAmbientPressureData
```

## Overview

Use SensorKit’s [`ambientPressure`](../SensorKit/srsensor/ambientpressure.md) sensor to read ambient pressure data.

## Topics

### Instance Properties
- [var identifier: UInt64](./cmrecordedpressuredata/identifier.md)
  A value that uniquely identifies this measurement.
- [var startDate: Date](./cmrecordedpressuredata/startdate.md)
  The time and date when the system recorded the measurement.

## Relationships

### Inherits From
- [CMAmbientPressureData](./cmambientpressuredata.md)
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

### Ambient pressure
- [class CMAmbientPressureData](./cmambientpressuredata.md)
  A measurement of the ambient pressure and temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata)*