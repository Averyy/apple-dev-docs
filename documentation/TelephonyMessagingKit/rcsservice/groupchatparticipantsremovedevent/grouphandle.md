# groupHandle

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The group handle from which participants were removed.

**Availability**:
- iOS 26.0+

## Declaration

```swift
let groupHandle: RCSHandle.Group
```

## See Also

### Accessing event properties
- [let cellularServiceID: CellularServiceID](./cellularserviceid.md)
  Cellular service identifier associated with this event.
- [let removedParticipants: [RCSHandle.URI]](./removedparticipants.md)
  Array of handles indicating the participants that were removed.
- [let removedBy: RCSHandle.URI](./removedby.md)
  Handle of device that performed the operation.
- [let removedCurrentUser: Bool](./removedcurrentuser.md)
  Whether the current user was removed from the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatparticipantsremovedevent/grouphandle)*