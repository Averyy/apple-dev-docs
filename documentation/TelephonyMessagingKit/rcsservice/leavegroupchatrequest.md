# RCSService.LeaveGroupChatRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing a request to leave a group chat.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct LeaveGroupChatRequest
```

## Topics

### Creating a leave group chat request
- [init(cellularServiceID: CellularServiceID, groupHandle: RCSHandle.Group)](rcsservice/leavegroupchatrequest/init(cellularserviceid:grouphandle:).md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](rcsservice/leavegroupchatrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var groupHandle: RCSHandle.Group](rcsservice/leavegroupchatrequest/grouphandle.md)
  Group handle indicating the group to leave.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func createGroupChat(RCSService.CreateGroupChatRequest) async throws -> RCSService.CreateGroupChatRequest.Result](rcsservice/creategroupchat(_:).md)
  Creates a group with a list of participants and a specified subject.
- [RCSService.CreateGroupChatRequest](rcsservice/creategroupchatrequest.md)
  Structure representing a request for creating a group chat.
- [func leaveGroupChat(RCSService.LeaveGroupChatRequest) async throws](rcsservice/leavegroupchat(_:).md)
  Leave a group chat.
- [func addGroupChatParticipants(RCSService.AddGroupChatParticipantsRequest) async throws -> RCSService.AddGroupChatParticipantsRequest.Result](rcsservice/addgroupchatparticipants(_:).md)
  Adds participants to a group chat.
- [RCSService.AddGroupChatParticipantsRequest](rcsservice/addgroupchatparticipantsrequest.md)
  Structure representing a request for adding participants to a group chat.
- [func removeGroupChatParticipants(RCSService.RemoveGroupChatParticipantsRequest) async throws -> RCSService.RemoveGroupChatParticipantsRequest.Result](rcsservice/removegroupchatparticipants(_:).md)
  Removes participants from a group chat.
- [RCSService.RemoveGroupChatParticipantsRequest](rcsservice/removegroupchatparticipantsrequest.md)
  Structure representing a request for removing participants from a group chat.
- [func changeGroupChatSubject(RCSService.ChangeGroupChatSubjectRequest) async throws](rcsservice/changegroupchatsubject(_:).md)
  Changes subject of a group.
- [RCSService.ChangeGroupChatSubjectRequest](rcsservice/changegroupchatsubjectrequest.md)
  Structure representing a request for changing a group chat’s subject.
- [var groupChatEvents: some AsyncSequence<RCSService.GroupChatEvent, Never>](rcsservice/groupchatevents.md)
  Returns an asynchronous sequence of incoming group chat notifications produced by this service.
- [RCSService.GroupChatEvent](rcsservice/groupchatevent.md)
  Enumeration representing an RCS group chat event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/leavegroupchatrequest)*