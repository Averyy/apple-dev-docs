# averageActivePace

**Framework**: Core Motion  
**Kind**: property

The average pace of the user, measured in seconds per meter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 3.0+

## Declaration

```swift
var averageActivePace: NSNumber? { get }
```

#### Discussion

During regular updates, this property is set to the user’s average active pace since [`startUpdates(from:withHandler:)`](cmpedometer/startupdates(from:withhandler:).md) was called. When you perform historical queries, the property is set to the average active pace between [`startDate`](cmpedometerdata/startdate.md) and [`endDate`](cmpedometerdata/enddate.md).

The property averages the user’s pace only during periods of activity and it omits all periods of inactivity. The value of this property is `nil` when you are performing a query for historical pedometer data and the information is not available (such as when the user did not move between `startDate` and `endDate`). This property is also `nil` for devices that do not support the gathering of pace data.

## See Also

- [var numberOfSteps: NSNumber](cmpedometerdata/numberofsteps.md)
  The number of steps taken by the user.
- [var distance: NSNumber?](cmpedometerdata/distance.md)
  The estimated distance (in meters) traveled by the user.
- [var currentPace: NSNumber?](cmpedometerdata/currentpace.md)
  The current pace of the user, measured in seconds per meter.
- [var currentCadence: NSNumber?](cmpedometerdata/currentcadence.md)
  The rate at which steps are taken, measured in steps per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/averageactivepace)*