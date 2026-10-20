# CLKComplicationTimelineAnimationBehavior.always

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

Always animate transitions. During Time Travel, ClockKit creates animations between all entries, regardless of the values of their group identifiers.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
case always
```

```c
CLKComplicationTimelineAnimationBehaviorAlways
```

## See Also

### Constants
- [CLKComplicationTimelineAnimationBehavior.never](./never.md)
  No animations. This is the default behavior.
- [CLKComplicationTimelineAnimationBehavior.grouped](./grouped.md)
  Animations between groups. During Time Travel, ClockKit creates animations when transitioning between entries with different group identifiers. For entries with identical group identifiers, the new entry is displayed without animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/always)*