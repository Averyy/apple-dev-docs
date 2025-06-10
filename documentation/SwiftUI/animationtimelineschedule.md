# AnimationTimelineSchedule

**Framework**: SwiftUI  
**Kind**: struct

A pausable schedule of dates updating at a frequency no more quickly than the provided interval.

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
struct AnimationTimelineSchedule
```

#### Overview

You can also use [`animation(minimumInterval:paused:)`](timelineschedule/animation(minimuminterval:paused:).md) to construct this schedule.

## Topics

### Creating a schedule
- [init(minimumInterval: Double?, paused: Bool)](animationtimelineschedule/init(minimuminterval:paused:).md)
  Create a pausable schedule of dates updating at a frequency no more quickly than the provided interval.
### Getting the sequence of dates
- [func entries(from: Date, mode: TimelineScheduleMode) -> AnimationTimelineSchedule.Entries](animationtimelineschedule/entries(from:mode:).md)
  Returns entries at the frequency of the animation schedule.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TimelineSchedule](timelineschedule.md)

## See Also

- [struct EveryMinuteTimelineSchedule](everyminutetimelineschedule.md)
  A schedule for updating a timeline view at the start of every minute.
- [struct ExplicitTimelineSchedule](explicittimelineschedule.md)
  A schedule for updating a timeline view at explicit points in time.
- [struct PeriodicTimelineSchedule](periodictimelineschedule.md)
  A schedule for updating a timeline view at regular intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationtimelineschedule)*