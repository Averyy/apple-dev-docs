# RCSService.GroupChatParticipantsAddedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Event triggered when participants are added to a group.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct GroupChatParticipantsAddedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](./groupchatparticipantsaddedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](./groupchatparticipantsaddedevent/grouphandle.md)
  The group handle to which participants were added.
- [let addedParticipants: [RCSHandle.URI]](./groupchatparticipantsaddedevent/addedparticipants.md)
  Array of handles indicating the participants that were added.
- [let addedBy: RCSHandle.URI](./groupchatparticipantsaddedevent/addedby.md)
  Handle of device that performed the operation.
### Supporting RCS encryption
- [let isEndToEndEncrypted: Bool](./groupchatparticipantsaddedevent/isendtoendencrypted.md)
  A Boolean value that indicates whether the associated group is end-to-end encrypted.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [RCSService.GroupChatEndedEvent](./groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [RCSService.GroupChatParticipantsRemovedEvent](./groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatStartedEvent](./groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](./groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsaddedevent)*