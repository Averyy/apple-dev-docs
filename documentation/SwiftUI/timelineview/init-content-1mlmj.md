# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new timeline view that uses the given schedule.

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
nonisolated
init(_ schedule: Schedule, @ViewBuilder content: @escaping (TimelineViewDefaultContext) -> Content)
```

## Parameters

- `schedule`: A schedule that produces a sequence of dates that   indicate the instances when the view should update.   Use a type that conforms to  , like   , or a custom timeline schedule   that you define.
- `content`: A closure that generates view content at the moments   indicated by the schedule. The closure takes an input of type    that includes the date from the schedule that   prompted the update, as well as a    value that the view can use to customize its appearance.

## See Also

- [TimelineView.Context](timelineview/context.md)
  Information passed to a timeline view’s content callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineview/init(_:content:)-1mlmj)*