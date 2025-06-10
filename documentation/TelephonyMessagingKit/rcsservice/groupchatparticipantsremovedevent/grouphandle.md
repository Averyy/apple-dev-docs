# groupHandle

**Framework**: TelephonyMessagingKit  
**Kind**: property

The group handle from which participants were removed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let groupHandle: RCSHandle.Group
```

## See Also

- [let cellularServiceID: CellularServiceID](rcsservice/groupchatparticipantsremovedevent/cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let removedParticipants: [RCSHandle.URI]](rcsservice/groupchatparticipantsremovedevent/removedparticipants.md)
  Array of handles indicating the participants that were removed.
- [let removedBy: RCSHandle.URI](rcsservice/groupchatparticipantsremovedevent/removedby.md)
  Handle of device that performed the operation.
- [let removedCurrentUser: Bool](rcsservice/groupchatparticipantsremovedevent/removedcurrentuser.md)
  Whether the current user was removed from the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsremovedevent/grouphandle)*