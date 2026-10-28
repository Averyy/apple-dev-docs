# TimelineView.Context.Cadence

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

A rate at which timeline views can receive updates.

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
enum Cadence
```

## Overview

Use the cadence presented to content in a [`TimelineView`](../../timelineview.md) to hide information that updates faster than the view’s current update rate. For example, you could hide the millisecond component of a digital timer when the cadence is [`TimelineView.Context.Cadence.seconds`](./cadence-swift.enum/seconds.md) or [`TimelineView.Context.Cadence.minutes`](./cadence-swift.enum/minutes.md).

Because this enumeration conforms to the [`Comparable`](../../../Swift/comparable.md) protocol, you can compare cadences with relational operators. Slower cadences have higher values, so you could perform the check described above with the following comparison:

```swift
let hideMilliseconds = cadence > .live
```

## Topics

### Getting cadences
- [TimelineView.Context.Cadence.live](./cadence-swift.enum/live.md)
  Updates the view continuously.
- [TimelineView.Context.Cadence.seconds](./cadence-swift.enum/seconds.md)
  Updates the view approximately once per second.
- [TimelineView.Context.Cadence.minutes](./cadence-swift.enum/minutes.md)
  Updates the view approximately once per minute.

## Relationships

### Conforms To
- [Comparable](../../../Swift/comparable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the cadence
- [let cadence: TimelineView<Schedule, Content>.Context.Cadence](./cadence-swift.property.md)
  The rate at which the timeline updates the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineview/context/cadence-swift.enum)*