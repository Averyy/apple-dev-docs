# CLKComplicationTimelineAnimationBehavior.always

**Framework**: ClockKit  
**Kind**: case

Always animate transitions. During Time Travel, ClockKit creates animations between all entries, regardless of the values of their group identifiers.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
case always
```

## See Also

- [CLKComplicationTimelineAnimationBehavior.never](clkcomplicationtimelineanimationbehavior/never.md)
  No animations. This is the default behavior.
- [CLKComplicationTimelineAnimationBehavior.grouped](clkcomplicationtimelineanimationbehavior/grouped.md)
  Animations between groups. During Time Travel, ClockKit creates animations when transitioning between entries with different group identifiers. For entries with identical group identifiers, the new entry is displayed without animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/always)*