# date

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The time at which to display the entry.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var date: Date { get set }
```

```objc
@property (nonatomic, retain) NSDate * date;
```

## Mentions

- [Loading future timeline events](../loading-future-timeline-events.md)

#### Discussion

The date you specify represents the day and time at which to begin displaying the associated complication data. Set this value appropriately based on the data you want to display. For example, weather forecast data would use the time at which the forecast was valid, but information about an upcoming meeting would use an earlier date to give the user advance notice.

## See Also

### Setting the Entry Values
- [var complicationTemplate: CLKComplicationTemplate](./complicationtemplate.md)
  The template containing the data to display in your complication.
- [var timelineAnimationGroup: String?](./timelineanimationgroup.md)
  The animation group to which the entry belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/date)*