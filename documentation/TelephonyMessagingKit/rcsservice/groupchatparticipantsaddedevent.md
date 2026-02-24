# RCSService.GroupChatParticipantsAddedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Event triggered when participants are added to a group.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct GroupChatParticipantsAddedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](rcsservice/groupchatparticipantsaddedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatparticipantsaddedevent/grouphandle.md)
  The group handle to which participants were added.
- [let addedParticipants: [RCSHandle.URI]](rcsservice/groupchatparticipantsaddedevent/addedparticipants.md)
  Array of handles indicating the participants that were added.
- [let addedBy: RCSHandle.URI](rcsservice/groupchatparticipantsaddedevent/addedby.md)
  Handle of device that performed the operation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.GroupChatEndedEvent](rcsservice/groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [RCSService.GroupChatParticipantsRemovedEvent](rcsservice/groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatStartedEvent](rcsservice/groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](rcsservice/groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsaddedevent)*