# CMHighFrequencyHeartRateData

**Framework**: Core Motion  
**Kind**: class

A class that represents heart rate data collected at 1 Hz.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 10.0+

## Declaration

```swift
class CMHighFrequencyHeartRateData
```

#### Overview

Use the [`heartRate`](cmhighfrequencyheartratedata/heartrate.md) property to get the data, and the [`confidence`](cmhighfrequencyheartratedata/confidence.md) property for the accuracy.

## Topics

### Accessing heart rate data
- [var heartRate: Double](cmhighfrequencyheartratedata/heartrate.md)
  The heart rate value in units of beats per minute (BPM).
- [var confidence: CMHighFrequencyHeartRateDataConfidence](cmhighfrequencyheartratedata/confidence.md)
  The confidence level of the heart rate value.
- [enum CMHighFrequencyHeartRateDataConfidence](cmhighfrequencyheartratedataconfidence.md)
  The level of confidence in the accuracy of the heart rate data.
### Getting the sample date
- [var date: Date?](cmhighfrequencyheartratedata/date.md)
  The time the heart rate value occurs.

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

- [class CMPedometer](cmpedometer.md)
  An object for fetching the system-generated live walking data.
- [class CMPedometerData](cmpedometerdata.md)
  Information about the distance traveled by a user on foot.
- [class CMPedometerEvent](cmpedometerevent.md)
  A change in the user’s pedestrian activity.
- [class CMStepCounter](cmstepcounter.md)
  The number of steps the user has taken with the device.
- [class CMOdometerData](cmodometerdata.md)
  A class that represents odometer data for workouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata)*