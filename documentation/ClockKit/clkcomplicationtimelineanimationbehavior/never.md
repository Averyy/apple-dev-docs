# CLKComplicationTimelineAnimationBehavior.never

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

No animations. This is the default behavior.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
case never
```

```c
CLKComplicationTimelineAnimationBehaviorNever
```

## See Also

### Constants
- [CLKComplicationTimelineAnimationBehavior.grouped](./grouped.md)
  Animations between groups. During Time Travel, ClockKit creates animations when transitioning between entries with different group identifiers. For entries with identical group identifiers, the new entry is displayed without animations.
- [CLKComplicationTimelineAnimationBehavior.always](./always.md)
  Always animate transitions. During Time Travel, ClockKit creates animations between all entries, regardless of the values of their group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/never)*