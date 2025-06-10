# TimelineScheduleMode

**Framework**: SwiftUI  
**Kind**: enum

A mode of operation for timeline schedule updates.

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
enum TimelineScheduleMode
```

#### Overview

A [`TimelineView`](timelineview.md) provides a mode when calling its schedule’s [`entries(from:mode:)`](timelineschedule/entries(from:mode:).md) method. The view chooses a mode based on the state of the system. For example, a watchOS view might request a lower frequency of updates, using the [`TimelineScheduleMode.lowFrequency`](timelineschedulemode/lowfrequency.md) mode, when the user lowers their wrist.

## Topics

### Getting timeline schedule modes
- [TimelineScheduleMode.normal](timelineschedulemode/normal.md)
  A mode that produces schedule updates at the schedule’s natural cadence.
- [TimelineScheduleMode.lowFrequency](timelineschedulemode/lowfrequency.md)
  A mode that produces schedule updates at a reduced rate.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TimelineSchedule.Mode](timelineschedule/mode.md)
  An alias for the timeline schedule update mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedulemode)*