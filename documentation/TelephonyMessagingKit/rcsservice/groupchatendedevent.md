# RCSService.GroupChatEndedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Event triggered when a group chat is ended.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct GroupChatEndedEvent
```

## Topics

### Accessing event properties
- [let cellularServiceID: CellularServiceID](./groupchatendedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [struct CellularServiceID](../cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let groupHandle: RCSHandle.Group](./groupchatendedevent/grouphandle.md)
  The group handle of the group chat.
- [RCSHandle.Group](../rcshandle/group.md)
  A structure that represents an RCS group handle.
- [let endedBy: RCSHandle.URI](./groupchatendedevent/endedby.md)
  Handle of device that performed the operation.
- [RCSHandle.URI](../rcshandle/uri.md)
  A structure that represents an RCS URI handle.
### Instance Properties
- [let isEndToEndEncrypted: Bool](./groupchatendedevent/isendtoendencrypted.md)
  A Boolean value that indicates whether the associated group is end-to-end encrypted.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [RCSService.GroupChatParticipantsAddedEvent](./groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [RCSService.GroupChatParticipantsRemovedEvent](./groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatStartedEvent](./groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](./groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatendedevent)*