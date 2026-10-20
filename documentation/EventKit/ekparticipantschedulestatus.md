# EKParticipantScheduleStatus

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The participant’s scheduled status.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKParticipantScheduleStatus
```

```c
enum EKParticipantScheduleStatus : NSInteger;
```

## Topics

### Constants
- [EKParticipantScheduleStatus.none](./ekparticipantschedulestatus/none.md)
  The invitation hasn’t been sent yet.
- [EKParticipantScheduleStatus.pending](./ekparticipantschedulestatus/pending.md)
  The invitation is in the process of being sent.
- [EKParticipantScheduleStatus.sent](./ekparticipantschedulestatus/sent.md)
  The invitation has been sent, but it’s unclear if it was successfully delivered.
- [EKParticipantScheduleStatus.delivered](./ekparticipantschedulestatus/delivered.md)
  The invitation has been sent and successfully delivered.
- [EKParticipantScheduleStatus.recipientNotRecognized](./ekparticipantschedulestatus/recipientnotrecognized.md)
  The invitation wasn’t delivered because the source doesn’t recognize the recipient.
- [EKParticipantScheduleStatus.noPrivileges](./ekparticipantschedulestatus/noprivileges.md)
  The invitation wasn’t delivered because of insufficient privileges.
- [EKParticipantScheduleStatus.deliveryFailed](./ekparticipantschedulestatus/deliveryfailed.md)
  The invitation wasn’t delivered due to a temporary failure.
- [EKParticipantScheduleStatus.cannotDeliver](./ekparticipantschedulestatus/cannotdeliver.md)
  The invitation wasn’t delivered because the system is unsure of how to deliver it.
- [EKParticipantScheduleStatus.recipientNotAllowed](./ekparticipantschedulestatus/recipientnotallowed.md)
  The invitation wasn’t delivered because scheduling with the participant isn’t allowed.
### Initializers
- [init?(rawValue: Int)](./ekparticipantschedulestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining Participants
- [enum EKParticipantRole](./ekparticipantrole.md)
  The participant’s role for an event.
- [enum EKParticipantType](./ekparticipanttype.md)
  The type of participant.
- [enum EKParticipantStatus](./ekparticipantstatus.md)
  The participant’s attendance status for an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus)*