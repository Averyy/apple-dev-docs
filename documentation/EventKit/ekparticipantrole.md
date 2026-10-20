# EKParticipantRole

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The participant’s role for an event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKParticipantRole
```

```c
enum EKParticipantRole : NSInteger;
```

## Topics

### Constants
- [EKParticipantRole.unknown](./ekparticipantrole/unknown.md)
  The participant’s role is unknown.
- [EKParticipantRole.required](./ekparticipantrole/required.md)
  The participant’s attendance is required.
- [EKParticipantRole.optional](./ekparticipantrole/optional.md)
  The participant’s attendance is optional.
- [EKParticipantRole.chair](./ekparticipantrole/chair.md)
  The participant is the chair of the event.
- [EKParticipantRole.nonParticipant](./ekparticipantrole/nonparticipant.md)
  The participant does not have an active role in the event.
### Initializers
- [init?(rawValue: Int)](./ekparticipantrole/init%28rawvalue%29.md)

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
- [enum EKParticipantType](./ekparticipanttype.md)
  The type of participant.
- [enum EKParticipantStatus](./ekparticipantstatus.md)
  The participant’s attendance status for an event.
- [enum EKParticipantScheduleStatus](./ekparticipantschedulestatus.md)
  The participant’s scheduled status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipantrole)*