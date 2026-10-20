# RCSService.GroupChatSubjectUpdatedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Event triggered when a group’s subject is updated.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct GroupChatSubjectUpdatedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](./groupchatsubjectupdatedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](./groupchatsubjectupdatedevent/grouphandle.md)
  The group handle whose subject was updated.
- [let newSubject: String](./groupchatsubjectupdatedevent/newsubject.md)
  The new subject for the group.
- [let changedBy: RCSHandle.URI](./groupchatsubjectupdatedevent/changedby.md)
  Handle of device that performed the operation.
### Supporting RCS encryption
- [let isEndToEndEncrypted: Bool](./groupchatsubjectupdatedevent/isendtoendencrypted.md)
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
- [RCSService.GroupChatStartedEvent](./groupchatstartedevent.md)
  Event triggered when group chat is started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatsubjectupdatedevent)*