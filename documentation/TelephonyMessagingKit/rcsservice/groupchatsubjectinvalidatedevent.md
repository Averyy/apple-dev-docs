# RCSService.GroupChatSubjectInvalidatedEvent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Event triggered when a group’s encryption state changes, which causes the group subject to be cleared on the server.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct GroupChatSubjectInvalidatedEvent
```

## Overview

Your app should call [`changeGroupChatSubject(_:)`](./changegroupchatsubject%28_%29.md) to restore the group’s subject. Failing to do so will leave the group without a subject.

You can ignore this event if the group was unnamed.

## Topics

### Instance Properties
- [let cellularServiceID: CellularServiceID](./groupchatsubjectinvalidatedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](./groupchatsubjectinvalidatedevent/grouphandle.md)
  The group handle whose subject was invalidated.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatsubjectinvalidatedevent)*