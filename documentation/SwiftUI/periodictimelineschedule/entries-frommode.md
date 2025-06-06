# entries(from:mode:)

**Framework**: SwiftUI  
**Kind**: method

Provides a sequence of periodic dates starting from around a given date.

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
func entries(from startDate: Date, mode: TimelineScheduleMode) -> PeriodicTimelineSchedule.Entries
```

#### Discussion

A [`TimelineView`](timelineview.md) that you create with a schedule calls this method to ask the schedule when to update its content. The method returns a sequence of equally spaced dates in increasing order that represent points in time when the timeline view should update.

The schedule defines its periodicity and phase aligment based on the parameters you pass to its [`init(from:by:)`](periodictimelineschedule/init(from:by:).md) initializer. For example, for a `startDate` and `interval` of `10:09:30` and `60` seconds, the schedule prepares to issue dates half past each minute. The `startDate` that you pass to the `entries(from:mode:)` method then dictates the first date of the sequence as the beginning of the interval that the start date overlaps. Continuing the example above, a start date of `10:34:45` causes the first sequence entry to be `10:34:30`, because that’s the start of the interval in which the start date appears.

## See Also

- [PeriodicTimelineSchedule.Entries](periodictimelineschedule/entries.md)
  The sequence of dates in periodic schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/periodictimelineschedule/entries(from:mode:))*