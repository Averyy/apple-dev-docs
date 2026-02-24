# RCSService.GroupChatEndedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Event triggered when a group chat is ended.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct GroupChatEndedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](rcsservice/groupchatendedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatendedevent/grouphandle.md)
  The group handle of the group chat.
- [RCSHandle.Group](rcshandle/group.md)
  A structure that represents an RCS group handle.
- [let endedBy: RCSHandle.URI](rcsservice/groupchatendedevent/endedby.md)
  Handle of device that performed the operation.
- [RCSHandle.URI](rcshandle/uri.md)
  A structure that represents an RCS URI handle.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSService.GroupChatParticipantsAddedEvent](rcsservice/groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [RCSService.GroupChatParticipantsRemovedEvent](rcsservice/groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatStartedEvent](rcsservice/groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](rcsservice/groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatendedevent)*