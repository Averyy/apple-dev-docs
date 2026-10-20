# EKParticipantScheduleStatus.none

**Framework**: EventKit  
**Kind**: case  
**Role**: Case

The invitation hasn’t been sent yet.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
case none
```

```c
EKParticipantScheduleStatusNone
```

## See Also

### Constants
- [EKParticipantScheduleStatus.pending](./pending.md)
  The invitation is in the process of being sent.
- [EKParticipantScheduleStatus.sent](./sent.md)
  The invitation has been sent, but it’s unclear if it was successfully delivered.
- [EKParticipantScheduleStatus.delivered](./delivered.md)
  The invitation has been sent and successfully delivered.
- [EKParticipantScheduleStatus.recipientNotRecognized](./recipientnotrecognized.md)
  The invitation wasn’t delivered because the source doesn’t recognize the recipient.
- [EKParticipantScheduleStatus.noPrivileges](./noprivileges.md)
  The invitation wasn’t delivered because of insufficient privileges.
- [EKParticipantScheduleStatus.deliveryFailed](./deliveryfailed.md)
  The invitation wasn’t delivered due to a temporary failure.
- [EKParticipantScheduleStatus.cannotDeliver](./cannotdeliver.md)
  The invitation wasn’t delivered because the system is unsure of how to deliver it.
- [EKParticipantScheduleStatus.recipientNotAllowed](./recipientnotallowed.md)
  The invitation wasn’t delivered because scheduling with the participant isn’t allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/none)*