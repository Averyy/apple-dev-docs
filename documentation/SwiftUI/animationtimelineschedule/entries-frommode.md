# entries(from:mode:)

**Framework**: SwiftUI  
**Kind**: method

Returns entries at the frequency of the animation schedule.

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
func entries(from start: Date, mode: TimelineScheduleMode) -> AnimationTimelineSchedule.Entries
```

#### Discussion

When in `.lowFrequency` mode, return no entries, effectively pausing the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationtimelineschedule/entries(from:mode:))*