# PeriodicTimelineSchedule.Entries

**Framework**: SwiftUI  
**Kind**: struct

The sequence of dates in periodic schedule.

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

The [`entries(from:mode:)`](periodictimelineschedule/entries(from:mode:).md) method returns a value of this type, which is a [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) of periodic dates in ascending order. A [`TimelineView`](timelineview.md) that you create updates its content at the moments in time corresponding to the dates included in the sequence.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func entries(from: Date, mode: TimelineScheduleMode) -> PeriodicTimelineSchedule.Entries](periodictimelineschedule/entries(from:mode:).md)
  Provides a sequence of periodic dates starting from around a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/periodictimelineschedule/entries)*