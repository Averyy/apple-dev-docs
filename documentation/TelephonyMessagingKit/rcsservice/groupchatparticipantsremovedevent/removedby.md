# removedBy

**Framework**: TelephonyMessagingKit  
**Kind**: property

Handle of device that performed the operation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let removedBy: RCSHandle.URI
```

## See Also

- [let cellularServiceID: CellularServiceID](rcsservice/groupchatparticipantsremovedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let groupHandle: RCSHandle.Group](rcsservice/groupchatparticipantsremovedevent/grouphandle.md)
  The group handle from which participants were removed.
- [let removedParticipants: [RCSHandle.URI]](rcsservice/groupchatparticipantsremovedevent/removedparticipants.md)
  Array of handles indicating the participants that were removed.
- [let removedCurrentUser: Bool](rcsservice/groupchatparticipantsremovedevent/removedcurrentuser.md)
  Whether the current user was removed from the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsremovedevent/removedby)*