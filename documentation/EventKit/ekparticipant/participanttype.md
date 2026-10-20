# participantType

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The participant’s type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var participantType: EKParticipantType { get }
```

```objc
@property (nonatomic, readonly) EKParticipantType participantType;
```

## See Also

### Related Documentation
- [enum EKParticipantType](../ekparticipanttype.md)
  The type of participant.
### Accessing Participant Properties
- [var isCurrentUser: Bool](./iscurrentuser.md)
  A Boolean value indicating whether this participant represents the owner of this account.
- [var name: String?](./name.md)
  The participant’s name.
- [var participantRole: EKParticipantRole](./participantrole.md)
  The participant’s role in the event.
- [var participantStatus: EKParticipantStatus](./participantstatus.md)
  The participant’s attendance status.
- [var url: URL](./url.md)
  The URL representing this participant.
- [var contactPredicate: NSPredicate](./contactpredicate.md)
  A predicate to use with the Contacts framework to retrieve the corresponding contact instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/participanttype)*