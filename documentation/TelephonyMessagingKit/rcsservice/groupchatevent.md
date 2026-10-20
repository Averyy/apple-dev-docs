# RCSService.GroupChatEvent

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration representing an RCS group chat event.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum GroupChatEvent
```

## Topics

### Chat life cycle events
- [case started(RCSService.GroupChatStartedEvent)](./groupchatevent/started%28_%29.md)
  Group chat started.
- [RCSService.GroupChatStartedEvent](./groupchatstartedevent.md)
  Event triggered when group chat is started.
- [case ended(RCSService.GroupChatEndedEvent)](./groupchatevent/ended%28_%29.md)
  Group chat ended.
- [RCSService.GroupChatEndedEvent](./groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [case subjectUpdated(RCSService.GroupChatSubjectUpdatedEvent)](./groupchatevent/subjectupdated%28_%29.md)
  Group chat’s subject was updated.
- [RCSService.GroupChatSubjectUpdatedEvent](./groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.
### Participant events
- [case participantsAdded(RCSService.GroupChatParticipantsAddedEvent)](./groupchatevent/participantsadded%28_%29.md)
  Participants have been added to a group chat.
- [RCSService.GroupChatParticipantsAddedEvent](./groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [case participantsRemoved(RCSService.GroupChatParticipantsRemovedEvent)](./groupchatevent/participantsremoved%28_%29.md)
  Participants have been removed from a group chat.
- [RCSService.GroupChatParticipantsRemovedEvent](./groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
### Enumeration Cases
- [case subjectInvalidated(RCSService.GroupChatSubjectInvalidatedEvent)](./groupchatevent/subjectinvalidated%28_%29.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var groupChatEvents: some AsyncSequence<RCSService.GroupChatEvent, Never>](./groupchatevents.md)
  Returns an asynchronous sequence of incoming group chat notifications produced by this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/groupchatevent)*