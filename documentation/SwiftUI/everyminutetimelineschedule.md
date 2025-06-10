# EveryMinuteTimelineSchedule

**Framework**: SwiftUI  
**Kind**: struct

A schedule for updating a timeline view at the start of every minute.

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
struct EveryMinuteTimelineSchedule
```

#### Overview

You can also use [`everyMinute`](timelineschedule/everyminute.md) to construct this schedule.

## Topics

### Creating a schedule
- [init()](everyminutetimelineschedule/init.md)
  Creates a per-minute update schedule.
### Getting the sequence of dates
- [func entries(from: Date, mode: TimelineScheduleMode) -> EveryMinuteTimelineSchedule.Entries](everyminutetimelineschedule/entries(from:mode:).md)
  Provides a sequence of per-minute dates starting from a given date.
- [EveryMinuteTimelineSchedule.Entries](everyminutetimelineschedule/entries.md)
  The sequence of dates in an every minute schedule.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TimelineSchedule](timelineschedule.md)

## See Also

- [struct AnimationTimelineSchedule](animationtimelineschedule.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [struct ExplicitTimelineSchedule](explicittimelineschedule.md)
  A schedule for updating a timeline view at explicit points in time.
- [struct PeriodicTimelineSchedule](periodictimelineschedule.md)
  A schedule for updating a timeline view at regular intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/everyminutetimelineschedule)*