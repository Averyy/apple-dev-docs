# timelineAnimationGroup

**Framework**: ClockKit  
**Kind**: property

The animation group to which the entry belongs.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var timelineAnimationGroup: String? { get set }
```

#### Discussion

Use animation groups to created animated transitions between some, but not all, timeline entries. During Time Travel, ClockKit creates transition animations between entries with different group identifiers. ClockKit also creates transitions between entries whose identifiers are both `nil`. When the group identifiers are the same, ClockKit doesn’t create transition animations.

The group identifier is used only to determine whether transition animations should be created. The contents of the string may be anything that helps you identify the group to your app.

## See Also

- [var date: Date](clkcomplicationtimelineentry/date.md)
  The time at which to display the entry.
- [var complicationTemplate: CLKComplicationTemplate](clkcomplicationtimelineentry/complicationtemplate.md)
  The template containing the data to display in your complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry/timelineanimationgroup)*