# CMPedometerEvent

**Framework**: Core Motion  
**Kind**: class

A change in the user’s pedestrian activity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CMPedometerEvent
```

## Topics

### Pedometer Data
- [var date: Date](cmpedometerevent/date.md)
  The date on which the pedometer event was recorded.
- [var type: CMPedometerEventType](cmpedometerevent/type.md)
  The type of change that occurred.
- [enum CMPedometerEventType](cmpedometereventtype.md)
  Constants indicating the change that occurred to the user’s pedestrian activity.
### Initializers
- [init?(coder: NSCoder)](cmpedometerevent/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
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

- [class CMPedometer](cmpedometer.md)
  An object for fetching the system-generated live walking data.
- [class CMPedometerData](cmpedometerdata.md)
  Information about the distance traveled by a user on foot.
- [class CMStepCounter](cmstepcounter.md)
  The number of steps the user has taken with the device.
- [class CMOdometerData](cmodometerdata.md)
  A class that represents odometer data for workouts.
- [class CMHighFrequencyHeartRateData](cmhighfrequencyheartratedata.md)
  A class that represents heart rate data collected at 1 Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerevent)*