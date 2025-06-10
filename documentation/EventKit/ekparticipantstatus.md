# EKParticipantStatus

**Framework**: EventKit  
**Kind**: enum

The participant’s attendance status for an event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKParticipantStatus
```

## Topics

### Constants
- [EKParticipantStatus.unknown](ekparticipantstatus/unknown.md)
  The participant’s attendance status is unknown.
- [EKParticipantStatus.pending](ekparticipantstatus/pending.md)
  The participant has yet to respond to the event.
- [EKParticipantStatus.accepted](ekparticipantstatus/accepted.md)
  The participant has accepted the event.
- [EKParticipantStatus.declined](ekparticipantstatus/declined.md)
  The participant has declined the event.
- [EKParticipantStatus.tentative](ekparticipantstatus/tentative.md)
  The participant’s attendance status is tentative.
- [EKParticipantStatus.delegated](ekparticipantstatus/delegated.md)
  The participant has delegated attendance to another participant.
- [EKParticipantStatus.completed](ekparticipantstatus/completed.md)
  The participant’s event has completed.
- [EKParticipantStatus.inProcess](ekparticipantstatus/inprocess.md)
  The participant’s event is currently in process.
### Initializers
- [init?(rawValue: Int)](ekparticipantstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum EKParticipantRole](ekparticipantrole.md)
  The participant’s role for an event.
- [enum EKParticipantType](ekparticipanttype.md)
  The type of participant.
- [enum EKParticipantScheduleStatus](ekparticipantschedulestatus.md)
  The participant’s scheduled status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipantstatus)*