# RCSService.RemoveGroupChatParticipantsRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing a request for removing participants from a group chat.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct RemoveGroupChatParticipantsRequest
```

## Topics

### Creating a remove group chat participants request
- [init(cellularServiceID: CellularServiceID, groupHandle: RCSHandle.Group, participants: [RCSHandle.URI])](rcsservice/removegroupchatparticipantsrequest/init(cellularserviceid:grouphandle:participants:).md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](rcsservice/removegroupchatparticipantsrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var groupHandle: RCSHandle.Group](rcsservice/removegroupchatparticipantsrequest/grouphandle.md)
  Group handle indicating the group from which to remove participants.
- [var participants: [RCSHandle.URI]](rcsservice/removegroupchatparticipantsrequest/participants.md)
  Array of participants to be removed from group.
### Accessing the request result
- [RCSService.RemoveGroupChatParticipantsRequest.Result](rcsservice/removegroupchatparticipantsrequest/result.md)
  Structure representing the result of a request to remove participants from a group chat.

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
- [RCSService.LeaveGroupChatRequest](rcsservice/leavegroupchatrequest.md)
  Structure representing a request to leave a group chat.
- [func addGroupChatParticipants(RCSService.AddGroupChatParticipantsRequest) async throws -> RCSService.AddGroupChatParticipantsRequest.Result](rcsservice/addgroupchatparticipants(_:).md)
  Adds participants to a group chat.
- [RCSService.AddGroupChatParticipantsRequest](rcsservice/addgroupchatparticipantsrequest.md)
  Structure representing a request for adding participants to a group chat.
- [func removeGroupChatParticipants(RCSService.RemoveGroupChatParticipantsRequest) async throws -> RCSService.RemoveGroupChatParticipantsRequest.Result](rcsservice/removegroupchatparticipants(_:).md)
  Removes participants from a group chat.
- [func changeGroupChatSubject(RCSService.ChangeGroupChatSubjectRequest) async throws](rcsservice/changegroupchatsubject(_:).md)
  Changes subject of a group.
- [RCSService.ChangeGroupChatSubjectRequest](rcsservice/changegroupchatsubjectrequest.md)
  Structure representing a request for changing a group chat’s subject.
- [var groupChatEvents: some AsyncSequence<RCSService.GroupChatEvent, Never>](rcsservice/groupchatevents.md)
  Returns an asynchronous sequence of incoming group chat notifications produced by this service.
- [RCSService.GroupChatEvent](rcsservice/groupchatevent.md)
  Enumeration representing an RCS group chat event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/removegroupchatparticipantsrequest)*