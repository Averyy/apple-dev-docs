# TimelineView.Context

**Framework**: SwiftUI  
**Kind**: struct

Information passed to a timeline view’s content callback.

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
struct Context
```

#### Overview

The context includes both the [`date`](timelineview/context/date.md) from the schedule that triggered the callback, and a [`cadence`](timelineview/context/cadence-swift.property.md) that you can use to customize the appearance of your view. For example, you might choose to display the second hand of an analog clock only when the cadence is [`TimelineView.Context.Cadence.seconds`](timelineview/context/cadence-swift.enum/seconds.md) or faster.

## Topics

### Getting the date
- [let date: Date](timelineview/context/date.md)
  The date from the schedule that triggered the current view update.
### Getting the cadence
- [let cadence: TimelineView<Schedule, Content>.Context.Cadence](timelineview/context/cadence-swift.property.md)
  The rate at which the timeline updates the view.
- [TimelineView.Context.Cadence](timelineview/context/cadence-swift.enum.md)
  A rate at which timeline views can receive updates.
### Invalidating the context
- [func invalidateTimelineContent()](timelineview/context/invalidatetimelinecontent.md)
  Resets any pre-rendered views the system has from the timeline.

## See Also

- [init(Schedule, content: (TimelineViewDefaultContext) -> Content)](timelineview/init(_:content:)-1mlmj.md)
  Creates a new timeline view that uses the given schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineview/context)*