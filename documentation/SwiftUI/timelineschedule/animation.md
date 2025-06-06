# animation

**Framework**: SwiftUI  
**Kind**: property

A pausable schedule of dates updating at a frequency no more quickly than the provided interval.

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
static var animation: AnimationTimelineSchedule { get }
```

## See Also

- [static func animation(minimumInterval: Double?, paused: Bool) -> AnimationTimelineSchedule](timelineschedule/animation(minimuminterval:paused:).md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [static var everyMinute: EveryMinuteTimelineSchedule](timelineschedule/everyminute.md)
  A schedule for updating a timeline view at the start of every minute.
- [static func explicit<S>(S) -> ExplicitTimelineSchedule<S>](timelineschedule/explicit(_:).md)
  A schedule for updating a timeline view at explicit points in time.
- [static func periodic(from: Date, by: TimeInterval) -> PeriodicTimelineSchedule](timelineschedule/periodic(from:by:).md)
  A schedule for updating a timeline view at regular intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedule/animation)*