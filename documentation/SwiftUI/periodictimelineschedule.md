# PeriodicTimelineSchedule

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A schedule for updating a timeline view at regular intervals.

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
struct PeriodicTimelineSchedule
```

## Overview

You can also use [`periodic(from:by:)`](./timelineschedule/periodic%28from,by%29.md) to construct this schedule.

## Topics

### Creating a schedule
- [init(from: Date, by: TimeInterval)](./periodictimelineschedule/init%28from,by%29.md)
  Creates a periodic update schedule.
### Getting the sequence of dates
- [func entries(from: Date, mode: TimelineScheduleMode) -> PeriodicTimelineSchedule.Entries](./periodictimelineschedule/entries%28from,mode%29.md)
  Provides a sequence of periodic dates starting from around a given date.
- [PeriodicTimelineSchedule.Entries](./periodictimelineschedule/entries.md)
  The sequence of dates in periodic schedule.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TimelineSchedule](./timelineschedule.md)

## See Also

### Supporting types
- [struct AnimationTimelineSchedule](./animationtimelineschedule.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [struct EveryMinuteTimelineSchedule](./everyminutetimelineschedule.md)
  A schedule for updating a timeline view at the start of every minute.
- [struct ExplicitTimelineSchedule](./explicittimelineschedule.md)
  A schedule for updating a timeline view at explicit points in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/periodictimelineschedule)*