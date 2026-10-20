# contactPredicate

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

A predicate to use with the Contacts framework to retrieve the corresponding contact instance.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var contactPredicate: NSPredicate { get }
```

```objc
@property (nonatomic, readonly) NSPredicate * contactPredicate;
```

#### Discussion

Use this property to get a predicate that you can use with a [`CNContactStore`](../../Contacts/cncontactstore.md) to fetch a [`CNContact`](../../Contacts/cncontact.md) instance for this participant, if one exists.

## See Also

### Accessing Participant Properties
- [var isCurrentUser: Bool](./iscurrentuser.md)
  A Boolean value indicating whether this participant represents the owner of this account.
- [var name: String?](./name.md)
  The participant’s name.
- [var participantRole: EKParticipantRole](./participantrole.md)
  The participant’s role in the event.
- [var participantStatus: EKParticipantStatus](./participantstatus.md)
  The participant’s attendance status.
- [var participantType: EKParticipantType](./participanttype.md)
  The participant’s type.
- [var url: URL](./url.md)
  The URL representing this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/contactpredicate)*