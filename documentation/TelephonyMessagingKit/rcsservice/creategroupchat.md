# createGroupChat(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Creates a group with a list of participants and a specified subject.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func createGroupChat(_ request: RCSService.CreateGroupChatRequest) async throws -> RCSService.CreateGroupChatRequest.Result
```

#### Return Value

`CreateGroupChatRequest.Result` containing the group handle for the group.

#### Discussion

> **Note**: - `RCSService.Error.notSupported` when messaging service does not support group chat.
- `RCSService.Error.maximumSizeExceeded` when group chat size exceeds the maximum allowed group size.

## Parameters

- `request`: Request specifying the group to create.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/creategroupchat(_:))*