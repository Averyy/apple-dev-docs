# createGroupChat(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method  
**Role**: Instance Method

Creates a group with a list of participants and a specified subject.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final func createGroupChat(_ request: RCSService.CreateGroupChatRequest) async throws -> RCSService.CreateGroupChatRequest.Result
```

#### Return Value

A [`RCSService.CreateGroupChatRequest.Result`](./creategroupchatrequest/result.md) that contains the group handle for the group.

#### Discussion

> **Throws**: If the messaging service doesn’t support group chat, this method throws [`RCSService.Error.notSupported`](./error/notsupported.md). If the group chat size exceeds the maximum allowed size, this method throws [`RCSService.Error.maximumSizeExceeded`](./error/maximumsizeexceeded.md).

## Parameters

- `request`: Request specifying the group to create.

## See Also

### Managing group chats
- [RCSService.CreateGroupChatRequest](./creategroupchatrequest.md)
  Structure representing a request for creating a group chat.
- [func leaveGroupChat(RCSService.LeaveGroupChatRequest) async throws](./leavegroupchat%28_%29.md)
  Leave a group chat.
- [RCSService.LeaveGroupChatRequest](./leavegroupchatrequest.md)
  Structure representing a request to leave a group chat.
- [func addGroupChatParticipants(RCSService.AddGroupChatParticipantsRequest) async throws -> RCSService.AddGroupChatParticipantsRequest.Result](./addgroupchatparticipants%28_%29.md)
  Adds participants to a group chat.
- [RCSService.AddGroupChatParticipantsRequest](./addgroupchatparticipantsrequest.md)
  Structure representing a request for adding participants to a group chat.
- [func removeGroupChatParticipants(RCSService.RemoveGroupChatParticipantsRequest) async throws -> RCSService.RemoveGroupChatParticipantsRequest.Result](./removegroupchatparticipants%28_%29.md)
  Removes participants from a group chat.
- [RCSService.RemoveGroupChatParticipantsRequest](./removegroupchatparticipantsrequest.md)
  Structure representing a request for removing participants from a group chat.
- [func changeGroupChatSubject(RCSService.ChangeGroupChatSubjectRequest) async throws](./changegroupchatsubject%28_%29.md)
  Changes subject of a group.
- [RCSService.ChangeGroupChatSubjectRequest](./changegroupchatsubjectrequest.md)
  Structure representing a request for changing a group chat’s subject.
- [var groupChatEvents: some AsyncSequence<RCSService.GroupChatEvent, Never>](./groupchatevents.md)
  Returns an asynchronous sequence of incoming group chat notifications produced by this service.
- [RCSService.GroupChatEvent](./groupchatevent.md)
  Enumeration representing an RCS group chat event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/creategroupchat(_:))*