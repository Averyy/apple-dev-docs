# animation(minimumInterval:paused:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
@export(implementation)
static func animation(minimumInterval: Double? = nil, paused: Bool = false) -> AnimationTimelineSchedule
```

Available when `Self` is `AnimationTimelineSchedule`.

## Parameters

- `minimumInterval`: The minimum interval to update the schedule at. Pass nil to let the system pick an appropriate update interval.
- `paused`: If the schedule should stop generating updates.

## See Also

### Getting built-in schedules
- [static var animation: AnimationTimelineSchedule](./animation.md)
  A pausable schedule of dates updating at a frequency no more quickly than the provided interval.
- [static var everyMinute: EveryMinuteTimelineSchedule](./everyminute.md)
  A schedule for updating a timeline view at the start of every minute.
- [static func explicit<S>(S) -> ExplicitTimelineSchedule<S>](./explicit%28_%29.md)
  A schedule for updating a timeline view at explicit points in time.
- [static func periodic(from: Date, by: TimeInterval) -> PeriodicTimelineSchedule](./periodic%28from,by%29.md)
  A schedule for updating a timeline view at regular intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedule/animation(minimuminterval:paused:))*