# RCSService.ChangeGroupChatSubjectRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure representing a request for changing a group chat’s subject.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct ChangeGroupChatSubjectRequest
```

## Topics

### Creating a change group chat subject request
- [init(cellularServiceID: CellularServiceID, groupHandle: RCSHandle.Group, newSubject: String)](./changegroupchatsubjectrequest/init%28cellularserviceid,grouphandle,newsubject%29.md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](./changegroupchatsubjectrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var groupHandle: RCSHandle.Group](./changegroupchatsubjectrequest/grouphandle.md)
  Group handle indicating the group for which to change the subject.
- [var newSubject: String](./changegroupchatsubjectrequest/newsubject.md)
  String specifying the new subject for the group.
### Supporting RCS encryption
- [var isEndToEndEncrypted: Bool](./changegroupchatsubjectrequest/isendtoendencrypted.md)
  A Boolean value indicating whether this request should be end-to-end encrypted. If the service does not support end-to-end encryption, the operation will throw [`RCSService.Error.endToEndEncryptionNotSupported`](./error/endtoendencryptionnotsupported.md).

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
- [var groupChatEvents: some AsyncSequence<RCSService.GroupChatEvent, Never>](./groupchatevents.md)
  Returns an asynchronous sequence of incoming group chat notifications produced by this service.
- [RCSService.GroupChatEvent](./groupchatevent.md)
  Enumeration representing an RCS group chat event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/changegroupchatsubjectrequest)*