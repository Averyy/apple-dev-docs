# cellularServiceID

**Framework**: TelephonyMessagingKit  
**Kind**: property

Cellular service identifier associated with this event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let cellularServiceID: CellularServiceID
```

## See Also

- [let groupHandle: RCSHandle.Group](rcsservice/groupchatparticipantsremovedevent/grouphandle.md)
  The group handle from which participants were removed.
- [let removedParticipants: [RCSHandle.URI]](rcsservice/groupchatparticipantsremovedevent/removedparticipants.md)
  Array of handles indicating the participants that were removed.
- [let removedBy: RCSHandle.URI](rcsservice/groupchatparticipantsremovedevent/removedby.md)
  Handle of device that performed the operation.
- [let removedCurrentUser: Bool](rcsservice/groupchatparticipantsremovedevent/removedcurrentuser.md)
  Whether the current user was removed from the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsremovedevent/cellularserviceid)*