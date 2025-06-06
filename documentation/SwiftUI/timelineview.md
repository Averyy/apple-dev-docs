# TimelineView

**Framework**: SwiftUI  
**Kind**: struct

A view that updates according to a schedule that you provide.

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
struct TimelineView<Schedule, Content> where Schedule : TimelineSchedule
```

#### Overview

A timeline view acts as a container with no appearance of its own. Instead, it redraws the content it contains at scheduled points in time. For example, you can update the face of an analog timer once per second:

```swift
TimelineView(.periodic(from: startDate, by: 1)) { context in
    AnalogTimerView(date: context.date)
}
```

The closure that creates the content receives an input of type [`TimelineView.Context`](timelineview/context.md) that you can use to customize the content’s appearance. The context includes the [`date`](timelineview/context/date.md) that triggered the update. In the example above, the timeline view sends that date to an analog timer that you create so the timer view knows how to draw the hands on its face.

The context also includes a [`cadence`](timelineview/context/cadence-swift.property.md) property that you can use to hide unnecessary detail. For example, you can use the cadence to decide when it’s appropriate to display the timer’s second hand:

```swift
TimelineView(.periodic(from: startDate, by: 1.0)) { context in
    AnalogTimerView(
        date: context.date,
        showSeconds: context.cadence <= .seconds)
}
```

The system might use a cadence that’s slower than the schedule’s update rate. For example, a view on watchOS might remain visible when the user lowers their wrist, but update less frequently, and thus require less detail.

You can define a custom schedule by creating a type that conforms to the [`TimelineSchedule`](timelineschedule.md) protocol, or use one of the built-in schedule types:

- Use an [`everyMinute`](timelineschedule/everyminute.md) schedule to update at the beginning of each minute.
- Use a [`periodic(from:by:)`](timelineschedule/periodic(from:by:).md) schedule to update periodically with a custom start time and interval between updates.
- Use an [`explicit(_:)`](timelineschedule/explicit(_:).md) schedule when you need a finite number, or irregular set of updates.

For a schedule containing only dates in the past, the timeline view shows the last date in the schedule. For a schedule containing only dates in the future, the timeline draws its content using the current date until the first scheduled date arrives.

## Topics

### Creating a timeline
- [init(Schedule, content: (TimelineViewDefaultContext) -> Content)](timelineview/init(_:content:)-1mlmj.md)
  Creates a new timeline view that uses the given schedule.
- [TimelineView.Context](timelineview/context.md)
  Information passed to a timeline view’s content callback.
### Deprecated symbols
- [init(Schedule, content: (TimelineView<Schedule, Content>.Context) -> Content)](timelineview/init(_:content:)-67h35.md)
  Creates a new timeline view that uses the given schedule.
### Initializers
- [init(_:content:)](timelineview/init(_:content:).md)
  Creates a new timeline view that uses the given schedule.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [View](view.md)

## See Also

- [Updating watchOS apps with timelines](../watchOS-Apps/updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [protocol TimelineSchedule](timelineschedule.md)
  A type that provides a sequence of dates for use as a schedule.
- [typealias TimelineViewDefaultContext](timelineviewdefaultcontext.md)
  Information passed to a timeline view’s content callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineview)*