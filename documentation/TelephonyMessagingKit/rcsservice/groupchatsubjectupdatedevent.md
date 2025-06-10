# RCSService.GroupChatSubjectUpdatedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Event triggered when a group’s subject is updated.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct GroupChatSubjectUpdatedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](rcsservice/groupchatsubjectupdatedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatsubjectupdatedevent/grouphandle.md)
  The group handle whose subject was updated.
- [let newSubject: String](rcsservice/groupchatsubjectupdatedevent/newsubject.md)
  The new subject for the group.
- [let changedBy: RCSHandle.URI](rcsservice/groupchatsubjectupdatedevent/changedby.md)
  Handle of device that performed the operation.

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
- [RCSService.GroupChatStartedEvent](rcsservice/groupchatstartedevent.md)
  Event triggered when group chat is started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatsubjectupdatedevent)*