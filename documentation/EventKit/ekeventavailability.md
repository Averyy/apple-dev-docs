# EKEventAvailability

**Framework**: EventKit  
**Kind**: enum

The event’s availability setting for scheduling purposes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKEventAvailability
```

## Topics

### Constants
- [EKEventAvailability.notSupported](ekeventavailability/notsupported.md)
  Availability settings are not supported by the event’s calendar.
- [EKEventAvailability.busy](ekeventavailability/busy.md)
  The event has a busy availability setting.
- [EKEventAvailability.free](ekeventavailability/free.md)
  The event has a free availability setting.
- [EKEventAvailability.tentative](ekeventavailability/tentative.md)
  The event has a tentative availability setting.
- [EKEventAvailability.unavailable](ekeventavailability/unavailable.md)
  The event has an unavailable availability setting.
### Initializers
- [init?(rawValue: Int)](ekeventavailability/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum EKEventStatus](ekeventstatus.md)
  The event’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventavailability)*