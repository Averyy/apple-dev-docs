# ExplicitTimelineSchedule

**Framework**: SwiftUI  
**Kind**: struct

A schedule for updating a timeline view at explicit points in time.

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
struct ExplicitTimelineSchedule<Entries> where Entries : Sequence, Entries.Element == Date
```

#### Overview

You can also use [`explicit(_:)`](timelineschedule/explicit(_:).md) to construct this schedule.

## Topics

### Creating a schedule
- [init(Entries)](explicittimelineschedule/init(_:).md)
  Creates a schedule composed of an explicit sequence of dates.
### Getting the sequence of dates
- [func entries(from: Date, mode: TimelineScheduleMode) -> Entries](explicittimelineschedule/entries(from:mode:).md)
  Provides the sequence of dates with which you initialized the schedule.

## Relationships

### Conforms To
- [TimelineSchedule](timelineschedule.md)

## See Also

- [struct AnimationTimelineSchedule](animationtimelineschedule.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [struct EveryMinuteTimelineSchedule](everyminutetimelineschedule.md)
  A schedule for updating a timeline view at the start of every minute.
- [struct PeriodicTimelineSchedule](periodictimelineschedule.md)
  A schedule for updating a timeline view at regular intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/explicittimelineschedule)*