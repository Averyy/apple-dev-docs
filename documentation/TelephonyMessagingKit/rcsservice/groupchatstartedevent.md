# RCSService.GroupChatStartedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Event triggered when group chat is started.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct GroupChatStartedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](./groupchatstartedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](./groupchatstartedevent/grouphandle.md)
  The group handle of the incoming group.
- [let participants: [RCSHandle.URI]](./groupchatstartedevent/participants.md)
  The current participants in the group.
- [let creator: RCSHandle.URI](./groupchatstartedevent/creator.md)
  Creator of group.
- [let subject: String](./groupchatstartedevent/subject.md)
  The group’s subject.
### Supporting RCS encryption
- [let isEndToEndEncrypted: Bool](./groupchatstartedevent/isendtoendencrypted.md)
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
- [RCSService.GroupChatParticipantsRemovedEvent](./groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatSubjectUpdatedEvent](./groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatstartedevent)*