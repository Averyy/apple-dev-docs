# RCSService.GroupChatStartedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Event triggered when group chat is started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct GroupChatStartedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](rcsservice/groupchatstartedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatstartedevent/grouphandle.md)
  The group handle of the incoming group.
- [let participants: [RCSHandle.URI]](rcsservice/groupchatstartedevent/participants.md)
  The current participants in the group.
- [let creator: RCSHandle.URI](rcsservice/groupchatstartedevent/creator.md)
  Creator of group.
- [let subject: String](rcsservice/groupchatstartedevent/subject.md)
  The group’s subject.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.GroupChatEndedEvent](rcsservice/groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [RCSService.GroupChatParticipantsAddedEvent](rcsservice/groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [RCSService.GroupChatParticipantsRemovedEvent](rcsservice/groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatSubjectUpdatedEvent](rcsservice/groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatstartedevent)*