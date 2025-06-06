# repeats

**Framework**: DeviceActivity  
**Kind**: property

A Boolean value that indicates whether the schedule recurs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var repeats: Bool { get }
```

#### Discussion

Use `repeats` to create an activity schedule that repeats until the activity-monitoring stops.

## See Also

- [init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents?)](deviceactivityschedule/init(intervalstart:intervalend:repeats:warningtime:).md)
  Creates a new schedule.
- [var intervalEnd: DateComponents](deviceactivityschedule/intervalend.md)
  The date components that represent the end time for a schedule’s interval.
- [var intervalStart: DateComponents](deviceactivityschedule/intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var nextInterval: DateInterval?](deviceactivityschedule/nextinterval.md)
  The schedule’s next interval or the current interval if one is ongoing.
- [var warningTime: DateComponents?](deviceactivityschedule/warningtime.md)
  Optional components that generate a warning prior to regularly scheduled events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule/repeats)*