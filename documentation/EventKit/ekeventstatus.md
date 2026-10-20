# EKEventStatus

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The event’s status.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKEventStatus
```

```c
enum EKEventStatus : NSInteger;
```

## Topics

### Constants
- [EKEventStatus.none](./ekeventstatus/none.md)
  The event has no status.
- [EKEventStatus.confirmed](./ekeventstatus/confirmed.md)
  The event is confirmed.
- [EKEventStatus.tentative](./ekeventstatus/tentative.md)
  The event is tentative.
- [EKEventStatus.canceled](./ekeventstatus/canceled.md)
  The event is canceled.
### Initializers
- [init?(rawValue: Int)](./ekeventstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scheduling Events
- [enum EKEventAvailability](./ekeventavailability.md)
  The event’s availability setting for scheduling purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstatus)*