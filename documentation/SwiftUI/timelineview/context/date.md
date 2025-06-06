# date

**Framework**: SwiftUI  
**Kind**: property

The date from the schedule that triggered the current view update.

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
let date: Date
```

#### Discussion

The first time a [`TimelineView`](timelineview.md) closure receives this date, it might be in the past. For example, if you create an [`everyMinute`](timelineschedule/everyminute.md) schedule at `10:09:55`, the schedule creates entries `10:09:00`, `10:10:00`, `10:11:00`, and so on. In response, the timeline view performs an initial update immediately, at `10:09:55`, but the context contains the `10:09:00` date entry. Subsequent entries arrive at their corresponding times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineview/context/date)*