# TimelineScheduleMode.lowFrequency

**Framework**: SwiftUI  
**Kind**: case

A mode that produces schedule updates at a reduced rate.

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
case lowFrequency
```

#### Discussion

In this mode, the schedule should generate only “major” updates, if possible. For example, a timeline providing updates to a timer might restrict updates to once a minute while in this mode.

## See Also

- [TimelineScheduleMode.normal](timelineschedulemode/normal.md)
  A mode that produces schedule updates at the schedule’s natural cadence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedulemode/lowfrequency)*