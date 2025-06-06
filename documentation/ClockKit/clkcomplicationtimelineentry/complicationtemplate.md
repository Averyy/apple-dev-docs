# complicationTemplate

**Framework**: ClockKit  
**Kind**: property

The template containing the data to display in your complication.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var complicationTemplate: CLKComplicationTemplate { get set }
```

#### Discussion

Specify a template that matches the style of complication for which you’re providing data. Different templates require different types of data. You must configure the template data before returning the timeline entry to ClockKit.

## See Also

- [var date: Date](clkcomplicationtimelineentry/date.md)
  The time at which to display the entry.
- [var timelineAnimationGroup: String?](clkcomplicationtimelineentry/timelineanimationgroup.md)
  The animation group to which the entry belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/complicationtemplate)*