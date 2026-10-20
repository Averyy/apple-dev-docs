# EKSpan

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

An object that indicates whether modifications should apply to a single event or all future events of a recurring event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKSpan
```

```c
enum EKSpan : NSInteger;
```

## Topics

### Constants
- [EKSpan.thisEvent](./ekspan/thisevent.md)
  Modifications to this event instance should affect only this instance.
- [EKSpan.futureEvents](./ekspan/futureevents.md)
  Modifications to this event instance should also affect future instances of this event.
### Initializers
- [init?(rawValue: Int)](./ekspan/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Basic Recurrence Rule
- [init(recurrenceWith: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd?)](./ekrecurrencerule/init%28recurrencewith,interval,end%29.md)
  Initializes and returns a simple recurrence rule with a given frequency, interval, and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekspan)*