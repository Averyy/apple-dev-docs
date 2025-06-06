# CLKComplicationTimelineAnimationBehavior.grouped

**Framework**: ClockKit  
**Kind**: case

Animations between groups. During Time Travel, ClockKit creates animations when transitioning between entries with different group identifiers. For entries with identical group identifiers, the new entry is displayed without animations.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
case grouped
```

## See Also

- [CLKComplicationTimelineAnimationBehavior.never](clkcomplicationtimelineanimationbehavior/never.md)
  No animations. This is the default behavior.
- [CLKComplicationTimelineAnimationBehavior.always](clkcomplicationtimelineanimationbehavior/always.md)
  Always animate transitions. During Time Travel, ClockKit creates animations between all entries, regardless of the values of their group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior/grouped)*