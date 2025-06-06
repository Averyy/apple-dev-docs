# CMPedometerData

**Framework**: Core Motion  
**Kind**: class

Information about the distance traveled by a user on foot.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
class CMPedometerData
```

#### Overview

You do not create instances of this class yourself. Instead, you use a [`CMPedometer`](cmpedometer.md) object to request pedometer data from the system. The data for each request is packaged into an instance of this class and delivered to the handlers you registered with the pedometer object.

## Topics

### Getting the Dates
- [var startDate: Date](cmpedometerdata/startdate.md)
  The start time for the pedometer data.
- [var endDate: Date](cmpedometerdata/enddate.md)
  The end time for the pedometer data.
### Getting the Pedestrian Data
- [var numberOfSteps: NSNumber](cmpedometerdata/numberofsteps.md)
  The number of steps taken by the user.
- [var distance: NSNumber?](cmpedometerdata/distance.md)
  The estimated distance (in meters) traveled by the user.
- [var averageActivePace: NSNumber?](cmpedometerdata/averageactivepace.md)
  The average pace of the user, measured in seconds per meter.
- [var currentPace: NSNumber?](cmpedometerdata/currentpace.md)
  The current pace of the user, measured in seconds per meter.
- [var currentCadence: NSNumber?](cmpedometerdata/currentcadence.md)
  The rate at which steps are taken, measured in steps per second.
### Getting the Floor Counts
- [var floorsAscended: NSNumber?](cmpedometerdata/floorsascended.md)
  The approximate number of floors ascended by walking.
- [var floorsDescended: NSNumber?](cmpedometerdata/floorsdescended.md)
  The approximate number of floors descended by walking.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class CMPedometerEvent](cmpedometerevent.md)
  A change in the user’s pedestrian activity.
- [class CMStepCounter](cmstepcounter.md)
  The number of steps the user has taken with the device.
- [class CMOdometerData](cmodometerdata.md)
  A class that represents odometer data for workouts.
- [class CMHighFrequencyHeartRateData](cmhighfrequencyheartratedata.md)
  A class that represents heart rate data collected at 1 Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata)*