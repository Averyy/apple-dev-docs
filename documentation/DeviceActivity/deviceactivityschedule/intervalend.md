# intervalEnd

**Framework**: DeviceActivity  
**Kind**: property

The date components that represent the end time for a schedule’s interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var intervalEnd: DateComponents { get }
```

#### Discussion

The system uses these components to compute `nextInterval.end`.

## See Also

- [init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents?)](deviceactivityschedule/init(intervalstart:intervalend:repeats:warningtime:).md)
  Creates a new schedule.
- [var intervalStart: DateComponents](deviceactivityschedule/intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var nextInterval: DateInterval?](deviceactivityschedule/nextinterval.md)
  The schedule’s next interval or the current interval if one is ongoing.
- [var repeats: Bool](deviceactivityschedule/repeats.md)
  A Boolean value that indicates whether the schedule recurs.
- [var warningTime: DateComponents?](deviceactivityschedule/warningtime.md)
  Optional components that generate a warning prior to regularly scheduled events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule/intervalend)*