# periodic(from:by:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
@export(implementation)
static func periodic(from startDate: Date, by interval: TimeInterval) -> PeriodicTimelineSchedule
```

Available when `Self` is `PeriodicTimelineSchedule`.

#### Discussion

Initialize a [`TimelineView`](../timelineview.md) with a periodic timeline schedule when you want to schedule timeline view updates periodically with a custom interval:

```swift
TimelineView(.periodic(from: startDate, by: 3.0)) { context in
    Text(context.date.description)
}
```

The timeline view updates its content at the start date, and then again at dates separated in time by the interval amount, which is every three seconds in the example above. For a start date in the past, the view updates immediately, providing as context the date corresponding to the most recent interval boundary. The view then refreshes normally at subsequent interval boundaries. For a start date in the future, the view updates once with the current date, and then begins regular updates at the start date.

The schedule defines the [`PeriodicTimelineSchedule.Entries`](../periodictimelineschedule/entries.md) structure to return the sequence of dates when the timeline view calls the [`entries(from:mode:)`](../periodictimelineschedule/entries%28from,mode%29.md) method.

## Parameters

- `startDate`: The date on which to start the sequence.
- `interval`: The time interval between successive sequence entries.

## See Also

### Getting built-in schedules
- [static var animation: AnimationTimelineSchedule](./animation.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [static func animation(minimumInterval: Double?, paused: Bool) -> AnimationTimelineSchedule](./animation%28minimuminterval,paused%29.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [static var everyMinute: EveryMinuteTimelineSchedule](./everyminute.md)
  A schedule for updating a timeline view at the start of every minute.
- [static func explicit<S>(S) -> ExplicitTimelineSchedule<S>](./explicit%28_%29.md)
  A schedule for updating a timeline view at explicit points in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedule/periodic(from:by:))*