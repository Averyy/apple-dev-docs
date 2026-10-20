# participantStatus

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The participant’s attendance status.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var participantStatus: EKParticipantStatus { get }
```

```objc
@property (nonatomic, readonly) EKParticipantStatus participantStatus;
```

## See Also

### Related Documentation
- [enum EKParticipantStatus](../ekparticipantstatus.md)
  The participant’s attendance status for an event.
### Accessing Participant Properties
- [var isCurrentUser: Bool](./iscurrentuser.md)
  A Boolean value indicating whether this participant represents the owner of this account.
- [var name: String?](./name.md)
  The participant’s name.
- [var participantRole: EKParticipantRole](./participantrole.md)
  The participant’s role in the event.
- [var participantType: EKParticipantType](./participanttype.md)
  The participant’s type.
- [var url: URL](./url.md)
  The URL representing this participant.
- [var contactPredicate: NSPredicate](./contactpredicate.md)
  A predicate to use with the Contacts framework to retrieve the corresponding contact instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/participantstatus)*