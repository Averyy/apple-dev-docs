# RCSService.GroupChatParticipantsRemovedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Event triggered when participants are removed from a group.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct GroupChatParticipantsRemovedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](./groupchatparticipantsremovedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](./groupchatparticipantsremovedevent/grouphandle.md)
  The group handle from which participants were removed.
- [let removedParticipants: [RCSHandle.URI]](./groupchatparticipantsremovedevent/removedparticipants.md)
  Array of handles indicating the participants that were removed.
- [let removedBy: RCSHandle.URI](./groupchatparticipantsremovedevent/removedby.md)
  Handle of device that performed the operation.
- [let removedCurrentUser: Bool](./groupchatparticipantsremovedevent/removedcurrentuser.md)
  Whether the current user was removed from the group.
### Supporting RCS encryption
- [let isEndToEndEncrypted: Bool](./groupchatparticipantsremovedevent/isendtoendencrypted.md)
  A Boolean value that indicates whether the associated group is end-to-end encrypted.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [RCSService.GroupChatEndedEvent](./groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [RCSService.GroupChatParticipantsAddedEvent](./groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [RCSService.GroupChatStartedEvent](./groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](./groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsremovedevent)*