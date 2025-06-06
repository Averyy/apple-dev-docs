# contactPredicate

**Framework**: EventKit  
**Kind**: property

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

#### Discussion

Use this property to get a predicate that you can use with a [`CNContactStore`](https://developer.apple.com/documentation/Contacts/CNContactStore) to fetch a [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) instance for this participant, if one exists.

## See Also

- [var isCurrentUser: Bool](ekparticipant/iscurrentuser.md)
  A Boolean value indicating whether this participant represents the owner of this account.
- [var name: String?](ekparticipant/name.md)
  The participant’s name.
- [var participantRole: EKParticipantRole](ekparticipant/participantrole.md)
  The participant’s role in the event.
- [var participantStatus: EKParticipantStatus](ekparticipant/participantstatus.md)
  The participant’s attendance status.
- [var participantType: EKParticipantType](ekparticipant/participanttype.md)
  The participant’s type.
- [var url: URL](ekparticipant/url.md)
  The URL representing this participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/contactpredicate)*