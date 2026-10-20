# PeriodicTimelineSchedule.Entries

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The sequence of dates in periodic schedule.

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
struct Entries
```

#### Overview

The [`entries(from:mode:)`](./entries%28from,mode%29.md) method returns a value of this type, which is a [`Sequence`](../../Swift/sequence.md) of periodic dates in ascending order. A [`TimelineView`](../timelineview.md) that you create updates its content at the moments in time corresponding to the dates included in the sequence.

## Relationships

### Conforms To
- [IteratorProtocol](../../Swift/iteratorprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Getting the sequence of dates
- [func entries(from: Date, mode: TimelineScheduleMode) -> PeriodicTimelineSchedule.Entries](./entries%28from,mode%29.md)
  Provides a sequence of periodic dates starting from around a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/periodictimelineschedule/entries)*