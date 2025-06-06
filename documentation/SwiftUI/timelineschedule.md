# TimelineSchedule

**Framework**: SwiftUI  
**Kind**: protocol

A type that provides a sequence of dates for use as a schedule.

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
protocol TimelineSchedule
```

#### Overview

Types that conform to this protocol implement a particular kind of schedule by defining an [`entries(from:mode:)`](timelineschedule/entries(from:mode:).md) method that returns a sequence of dates. Use a timeline schedule type when you initialize a [`TimelineView`](timelineview.md). For example, you can create a timeline view that updates every second, starting from some `startDate`, using a periodic schedule returned by [`periodic(from:by:)`](timelineschedule/periodic(from:by:).md):

```swift
TimelineView(.periodic(from: startDate, by: 1.0)) { context in
    // View content goes here.
}
```

You can also create custom timeline schedules. The timeline view updates its content according to the sequence of dates produced by the schedule.

## Topics

### Getting built-in schedules
- [static var animation: AnimationTimelineSchedule](timelineschedule/animation.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [static func animation(minimumInterval: Double?, paused: Bool) -> AnimationTimelineSchedule](timelineschedule/animation(minimuminterval:paused:).md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [static var everyMinute: EveryMinuteTimelineSchedule](timelineschedule/everyminute.md)
  A schedule for updating a timeline view at the start of every minute.
- [static func explicit<S>(S) -> ExplicitTimelineSchedule<S>](timelineschedule/explicit(_:).md)
  A schedule for updating a timeline view at explicit points in time.
- [static func periodic(from: Date, by: TimeInterval) -> PeriodicTimelineSchedule](timelineschedule/periodic(from:by:).md)
  A schedule for updating a timeline view at regular intervals.
### Getting a sequence of dates
- [func entries(from: Date, mode: Self.Mode) -> Self.Entries](timelineschedule/entries(from:mode:).md)
  Provides a sequence of dates starting around a given date.
- [associatedtype Entries : Sequence](timelineschedule/entries.md)
  The sequence of dates within a schedule.
### Specifying a mode
- [TimelineSchedule.Mode](timelineschedule/mode.md)
  An alias for the timeline schedule update mode.
- [enum TimelineScheduleMode](timelineschedulemode.md)
  A mode of operation for timeline schedule updates.
### Supporting types
- [struct AnimationTimelineSchedule](animationtimelineschedule.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [struct EveryMinuteTimelineSchedule](everyminutetimelineschedule.md)
  A schedule for updating a timeline view at the start of every minute.
- [struct ExplicitTimelineSchedule](explicittimelineschedule.md)
  A schedule for updating a timeline view at explicit points in time.
- [struct PeriodicTimelineSchedule](periodictimelineschedule.md)
  A schedule for updating a timeline view at regular intervals.

## Relationships

### Conforming Types
- [AnimationTimelineSchedule](animationtimelineschedule.md)
- [EveryMinuteTimelineSchedule](everyminutetimelineschedule.md)
- [ExplicitTimelineSchedule](explicittimelineschedule.md)
- [PeriodicTimelineSchedule](periodictimelineschedule.md)

## See Also

- [Updating watchOS apps with timelines](../watchOS-Apps/updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [struct TimelineView](timelineview.md)
  A view that updates according to a schedule that you provide.
- [typealias TimelineViewDefaultContext](timelineviewdefaultcontext.md)
  Information passed to a timeline view’s content callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedule)*