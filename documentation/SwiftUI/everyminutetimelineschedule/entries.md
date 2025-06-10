# EveryMinuteTimelineSchedule.Entries

**Framework**: SwiftUI  
**Kind**: struct

The sequence of dates in an every minute schedule.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Entries
```

#### Overview

The [`entries(from:mode:)`](everyminutetimelineschedule/entries(from:mode:).md) method returns a value of this type, which is a [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) of dates, one per minute, in ascending order. A [`TimelineView`](timelineview.md) that you create updates its content at the moments in time corresponding to the dates included in the sequence.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func entries(from: Date, mode: TimelineScheduleMode) -> EveryMinuteTimelineSchedule.Entries](everyminutetimelineschedule/entries(from:mode:).md)
  Provides a sequence of per-minute dates starting from a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/everyminutetimelineschedule/entries)*