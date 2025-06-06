# init(intervalStart:intervalEnd:repeats:warningTime:)

**Framework**: DeviceActivity  
**Kind**: init

Creates a new schedule.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents? = nil)
```

#### Discussion

> ❗ **Important**: If the current date falls in between [`intervalStart`](deviceactivityschedule/intervalstart.md) and [`intervalEnd`](deviceactivityschedule/intervalend.md), the system calls the [`intervalDidStart(for:)`](deviceactivitymonitor/intervaldidstart(for:).md) method immediately upon starting to monitor the activity. If the current date doesn’t fall in between `intervalStart` and `intervalEnd`, then `intervalDidStart(for:)` calls at the next date matching `intervalStart`.

If the current date falls in between [`intervalStart`](deviceactivityschedule/intervalstart.md) and [`intervalEnd`](deviceactivityschedule/intervalend.md), the system calls the [`intervalDidStart(for:)`](deviceactivitymonitor/intervaldidstart(for:).md) method immediately upon starting to monitor the activity. If the current date doesn’t fall in between `intervalStart` and `intervalEnd`, then `intervalDidStart(for:)` calls at the next date matching `intervalStart`.

## Parameters

- `intervalStart`: The date components that represent the start time for a schedule’s interval.
- `intervalEnd`: The date components that represent the end time for a schedule’s interval.
- `repeats`: Indicates whether the schedule recurs. If  , the extension   stops receiving callbacks when the interval ends for the first time.
- `warningTime`: An optional warning time to receive callbacks.   If the components specify a longer time interval than the schedule’s interval, the system   clamps the warning callbacks for each event’s threshold to the start time of the interval.

## See Also

- [var intervalEnd: DateComponents](deviceactivityschedule/intervalend.md)
  The date components that represent the end time for a schedule’s interval.
- [var intervalStart: DateComponents](deviceactivityschedule/intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var nextInterval: DateInterval?](deviceactivityschedule/nextinterval.md)
  The schedule’s next interval or the current interval if one is ongoing.
- [var repeats: Bool](deviceactivityschedule/repeats.md)
  A Boolean value that indicates whether the schedule recurs.
- [var warningTime: DateComponents?](deviceactivityschedule/warningtime.md)
  Optional components that generate a warning prior to regularly scheduled events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule/init(intervalstart:intervalend:repeats:warningtime:))*