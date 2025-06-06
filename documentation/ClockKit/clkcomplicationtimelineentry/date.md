# date

**Framework**: ClockKit  
**Kind**: property

The time at which to display the entry.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var date: Date { get set }
```

## Mentions

- [Loading future timeline events](loading-future-timeline-events.md)

#### Discussion

The date you specify represents the day and time at which to begin displaying the associated complication data. Set this value appropriately based on the data you want to display. For example, weather forecast data would use the time at which the forecast was valid, but information about an upcoming meeting would use an earlier date to give the user advance notice.

## See Also

- [var complicationTemplate: CLKComplicationTemplate](clkcomplicationtimelineentry/complicationtemplate.md)
  The template containing the data to display in your complication.
- [var timelineAnimationGroup: String?](clkcomplicationtimelineentry/timelineanimationgroup.md)
  The animation group to which the entry belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/date)*