# EKEventAvailability

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The event’s availability setting for scheduling purposes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKEventAvailability
```

```c
enum EKEventAvailability : NSInteger;
```

## Topics

### Constants
- [EKEventAvailability.notSupported](./ekeventavailability/notsupported.md)
  Availability settings are not supported by the event’s calendar.
- [EKEventAvailability.busy](./ekeventavailability/busy.md)
  The event has a busy availability setting.
- [EKEventAvailability.free](./ekeventavailability/free.md)
  The event has a free availability setting.
- [EKEventAvailability.tentative](./ekeventavailability/tentative.md)
  The event has a tentative availability setting.
- [EKEventAvailability.unavailable](./ekeventavailability/unavailable.md)
  The event has an unavailable availability setting.
### Initializers
- [init?(rawValue: Int)](./ekeventavailability/init%28rawvalue%29.md)

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
- [enum EKEventStatus](./ekeventstatus.md)
  The event’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventavailability)*