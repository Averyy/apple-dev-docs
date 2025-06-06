# entries(from:mode:)

**Framework**: SwiftUI  
**Kind**: method

Provides the sequence of dates with which you initialized the schedule.

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
func entries(from startDate: Date, mode: TimelineScheduleMode) -> Entries
```

#### Return Value

The sequence of dates that you provided at initialization.

#### Discussion

A [`TimelineView`](timelineview.md) that you create with a schedule calls this [`TimelineSchedule`](timelineschedule.md) method to ask the schedule when to update its content. The explicit timeline schedule implementation of this method returns the unmodified sequence of dates that you provided when you created the schedule with [`explicit(_:)`](timelineschedule/explicit(_:).md). As a result, this particular implementation ignores the `startDate` and `mode` parameters.

## Parameters

- `startDate`: The date from which the sequence begins. This   particular implementation of the protocol method ignores the start   date.
- `mode`: The mode for the update schedule. This particular   implementation of the protocol method ignores the mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/explicittimelineschedule/entries(from:mode:))*