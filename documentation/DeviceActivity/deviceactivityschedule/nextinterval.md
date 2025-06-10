# nextInterval

**Framework**: DeviceActivity  
**Kind**: property

The schedule’s next interval or the current interval if one is ongoing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var nextInterval: DateInterval? { get }
```

#### Discussion

`nil` if `intervalStart` and `intervalEnd` don’t match any future dates. The start and end dates indicate the earliest point when the [`intervalDidStart(for:)`](deviceactivitymonitor/intervaldidstart(for:).md) and [`intervalDidEnd(for:)`](deviceactivitymonitor/intervaldidend(for:).md) methods of your app extension’s principal class invokes. The system actually invokes these methods when someone uses the device during the interval. The system additionally calls [`intervalDidEnd(for:)`](deviceactivitymonitor/intervaldidend(for:).md) when you stop monitoring an activity with an ongoing interval. The system doesn’t call these methods unless the device is used during the interval.

> **Note**: This interval is computed using the provided date components and the [`Calendar.MatchingPolicy.nextTimePreservingSmallerComponents`](https://developer.apple.com/documentation/Foundation/Calendar/MatchingPolicy/nextTimePreservingSmallerComponents) policy for the `calendar` of both date components. If you don’t specify a calendar for either components, the system uses `Calendar.current`. The system bases the interval’s end date on wall-clock time, regardless of any time zone changes that occur during the interval.

## See Also

- [init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents?)](deviceactivityschedule/init(intervalstart:intervalend:repeats:warningtime:).md)
  Creates a new schedule.
- [var intervalEnd: DateComponents](deviceactivityschedule/intervalend.md)
  The date components that represent the end time for a schedule’s interval.
- [var intervalStart: DateComponents](deviceactivityschedule/intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var repeats: Bool](deviceactivityschedule/repeats.md)
  A Boolean value that indicates whether the schedule recurs.
- [var warningTime: DateComponents?](deviceactivityschedule/warningtime.md)
  Optional components that generate a warning prior to regularly scheduled events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule/nextinterval)*