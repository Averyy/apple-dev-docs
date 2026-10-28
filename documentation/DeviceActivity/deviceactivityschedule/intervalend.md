# intervalEnd

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

The date components that represent the end time for a schedule’s interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var intervalEnd: DateComponents { get }
```

## Discussion

The system uses these components to compute `nextInterval.end`.

## See Also

### Creating a Schedule
- [init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents?)](./init%28intervalstart,intervalend,repeats,warningtime%29.md)
  Creates a new schedule.
- [var intervalStart: DateComponents](./intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var nextInterval: DateInterval?](./nextinterval.md)
  The schedule’s next interval or the current interval if one is ongoing.
- [var repeats: Bool](./repeats.md)
  A Boolean value that indicates whether the schedule recurs.
- [var warningTime: DateComponents?](./warningtime.md)
  Optional components that generate a warning prior to regularly scheduled events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule/intervalend)*