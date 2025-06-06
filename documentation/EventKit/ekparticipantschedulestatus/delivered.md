# EKParticipantScheduleStatus.delivered

**Framework**: EventKit  
**Kind**: case

The invitation has been sent and successfully delivered.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case delivered
```

## See Also

- [EKParticipantScheduleStatus.none](ekparticipantschedulestatus/none.md)
  The invitation hasn’t been sent yet.
- [EKParticipantScheduleStatus.pending](ekparticipantschedulestatus/pending.md)
  The invitation is in the process of being sent.
- [EKParticipantScheduleStatus.sent](ekparticipantschedulestatus/sent.md)
  The invitation has been sent, but it’s unclear if it was successfully delivered.
- [EKParticipantScheduleStatus.recipientNotRecognized](ekparticipantschedulestatus/recipientnotrecognized.md)
  The invitation wasn’t delivered because the source doesn’t recognize the recipient.
- [EKParticipantScheduleStatus.noPrivileges](ekparticipantschedulestatus/noprivileges.md)
  The invitation wasn’t delivered because of insufficient privileges.
- [EKParticipantScheduleStatus.deliveryFailed](ekparticipantschedulestatus/deliveryfailed.md)
  The invitation wasn’t delivered due to a temporary failure.
- [EKParticipantScheduleStatus.cannotDeliver](ekparticipantschedulestatus/cannotdeliver.md)
  The invitation wasn’t delivered because the system is unsure of how to deliver it.
- [EKParticipantScheduleStatus.recipientNotAllowed](ekparticipantschedulestatus/recipientnotallowed.md)
  The invitation wasn’t delivered because scheduling with the participant isn’t allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipantschedulestatus/delivered)*