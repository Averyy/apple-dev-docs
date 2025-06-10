# RCSService.GroupChatParticipantsRemovedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Event triggered when participants are removed from a group.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct GroupChatParticipantsRemovedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](rcsservice/groupchatparticipantsremovedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatparticipantsremovedevent/grouphandle.md)
  The group handle from which participants were removed.
- [let removedParticipants: [RCSHandle.URI]](rcsservice/groupchatparticipantsremovedevent/removedparticipants.md)
  Array of handles indicating the participants that were removed.
- [let removedBy: RCSHandle.URI](rcsservice/groupchatparticipantsremovedevent/removedby.md)
  Handle of device that performed the operation.
- [let removedCurrentUser: Bool](rcsservice/groupchatparticipantsremovedevent/removedcurrentuser.md)
  Whether the current user was removed from the group.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.GroupChatEndedEvent](rcsservice/groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [RCSService.GroupChatParticipantsAddedEvent](rcsservice/groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [RCSService.GroupChatStartedEvent](rcsservice/groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](rcsservice/groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsremovedevent)*