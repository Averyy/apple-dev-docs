# RCSService.GroupChatSubjectInvalidatedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Event triggered when a group’s encryption state changes, which causes the group subject to be cleared on the server.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct GroupChatSubjectInvalidatedEvent
```

#### Overview

Your app should call [`changeGroupChatSubject(_:)`](rcsservice/changegroupchatsubject(_:).md) to restore the group’s subject. Failing to do so will leave the group without a subject.

You can ignore this event if the group was unnamed.

## Topics

### Instance Properties
- [let cellularServiceID: CellularServiceID](rcsservice/groupchatsubjectinvalidatedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatsubjectinvalidatedevent/grouphandle.md)
  The group handle whose subject was invalidated.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatsubjectinvalidatedevent)*