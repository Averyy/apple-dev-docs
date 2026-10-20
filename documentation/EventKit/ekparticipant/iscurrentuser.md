# isCurrentUser

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether this participant represents the owner of this account.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isCurrentUser: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCurrentUser) BOOL currentUser;
```

## See Also

### Related Documentation
- [Calendar and Reminders Programming Guide](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009765)
### Accessing Participant Properties
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
- [var contactPredicate: NSPredicate](./contactpredicate.md)
  A predicate to use with the Contacts framework to retrieve the corresponding contact instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant/iscurrentuser)*