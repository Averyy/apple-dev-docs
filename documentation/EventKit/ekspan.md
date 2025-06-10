# EKSpan

**Framework**: EventKit  
**Kind**: enum

An object that indicates whether modifications should apply to a single event or all future events of a recurring event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKSpan
```

## Topics

### Constants
- [EKSpan.thisEvent](ekspan/thisevent.md)
  Modifications to this event instance should affect only this instance.
- [EKSpan.futureEvents](ekspan/futureevents.md)
  Modifications to this event instance should also affect future instances of this event.
### Initializers
- [init?(rawValue: Int)](ekspan/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(recurrenceWith: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd?)](ekrecurrencerule/init(recurrencewith:interval:end:).md)
  Initializes and returns a simple recurrence rule with a given frequency, interval, and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekspan)*