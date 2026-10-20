# groupChatEvents

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

Returns an asynchronous sequence of incoming group chat notifications produced by this service.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final var groupChatEvents: some AsyncSequence<RCSService.GroupChatEvent, Never> { get throws }
```

## See Also

### Managing group chats
- [func createGroupChat(RCSService.CreateGroupChatRequest) async throws -> RCSService.CreateGroupChatRequest.Result](./creategroupchat%28_%29.md)
  Creates a group with a list of participants and a specified subject.
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
- [RCSService.GroupChatEvent](./groupchatevent.md)
  Enumeration representing an RCS group chat event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatevents)*