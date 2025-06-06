# warningTime

**Framework**: DeviceActivity  
**Kind**: property

Optional components that generate a warning prior to regularly scheduled events.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var warningTime: DateComponents? { get }
```

#### Discussion

You can create a warning time to notify your app extension ahead of time before the scheduled activity begins and ends. For instance, when your app schedules activity-monitoring from 10 a.m. to 11 a.m. for an event with a 30-minute threshold, setting the schedule’s warning time to 5 minutes results in the extension receiving [`intervalWillStartWarning(for:)`](deviceactivitymonitor/intervalwillstartwarning(for:).md), [`intervalWillEndWarning(for:)`](deviceactivitymonitor/intervalwillendwarning(for:).md), and [`eventWillReachThresholdWarning(_:activity:)`](deviceactivitymonitor/eventwillreachthresholdwarning(_:activity:).md) callbacks at 9:55 a.m., 10:55 a.m, and when 25 minutes of the event’s activity occurs, respectively. If the components specify a longer time interval than the schedule’s interval, the system clamps the warning callbacks for each event’s threshold to the start time of the interval.

## See Also

- [init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents?)](deviceactivityschedule/init(intervalstart:intervalend:repeats:warningtime:).md)
  Creates a new schedule.
- [var intervalEnd: DateComponents](deviceactivityschedule/intervalend.md)
  The date components that represent the end time for a schedule’s interval.
- [var intervalStart: DateComponents](deviceactivityschedule/intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var nextInterval: DateInterval?](deviceactivityschedule/nextinterval.md)
  The schedule’s next interval or the current interval if one is ongoing.
- [var repeats: Bool](deviceactivityschedule/repeats.md)
  A Boolean value that indicates whether the schedule recurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule/warningtime)*