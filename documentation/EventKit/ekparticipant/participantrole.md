# participantRole

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The participant’s role in the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var participantRole: EKParticipantRole { get }
```

```objc
@property (nonatomic, readonly) EKParticipantRole participantRole;
```

## See Also

### Related Documentation
- [enum EKParticipantRole](../ekparticipantrole.md)
  The participant’s role for an event.
### Accessing Participant Properties
- [var isCurrentUser: Bool](./iscurrentuser.md)
  A Boolean value indicating whether this participant represents the owner of this account.
- [var name: String?](./name.md)
  The participant’s name.
- [var participantStatus: EKParticipantStatus](./participantstatus.md)
  The participant’s attendance status.
- [var participantType: EKParticipantType](./participanttype.md)
  The participant’s type.
- [var url: URL](./url.md)
  The URL representing this participant.
- [var contactPredicate: NSPredicate](./contactpredicate.md)
  A predicate to use with the Contacts framework to retrieve the corresponding contact instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/participantrole)*