# RCSService

**Framework**: TelephonyMessagingKit  
**Kind**: class

A class that provides an interface for performing RCS operations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final class RCSService
```

## Mentions

- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)

#### Overview

Use the [`TelephonyMessagingSession`](telephonymessagingsession.md) property [`rcsService`](telephonymessagingsession/rcsservice.md) to get an instance of this class.

An `RCSService` sends and receives different kinds of messages, distinguished by the [`content`](rcsmessage/content-swift.property.md) property of [`RCSMessage`](rcsmessage.md):

Use the various overloads of `sendMessage(_:to:using:messageID)` to send messages of these types to recipients. The following example shows how to send a plain text message with [`sendMessage(_:to:using:messageID:)`](rcsservice/sendmessage(_:to:using:messageid:)-70q7h.md):

```swift
let service = TelephonyMessagingSession.shared.rcsService

let cellularServices = try TelephonyMessagingSession.shared.cellularServices
let cellularServiceID = cellularServices[0].id

guard service.isViable(for: cellularServiceID) else { return }

let message = RCSMessage.Text("Hello there.")
guard let handle = RCSHandle.phoneNumber(SAMPLE_PHONE_NUMBER) else { return }
try await service.sendMessage(message,
                   to: handle,
                   using:cellularServiceID,
                   messageID: RCSMessageID(rawValue: SAMPLE_RCS_MESSAGE_ID))
```

To receive messages, iterate over the [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md) asynchronous sequence with a `for`-`await`-`in` loop, then handle each notification based on its message content type, like this:

```swift
let service = TelephonyMessagingSession.shared.rcsService

let incomingMessageNotifications = try service.incomingMessageNotifications
Task {
    for await notification in incomingMessageNotifications {
        let receivedMessage = notification.message
        switch receivedMessage.content {
            case .text(let text): // ...
            case .fileTransfer(let fileTransfer): // ...
            case .geolocationPush(let geolocationPush): // ...
            case .dispositionNotification(let dispositionNotification): // ...
            case .composingIndicator(let composingIndicator): // ...
        }
    }
}
```

## Topics

### Determining service viabililty
- [func isViable(for: CellularServiceID) -> Bool](rcsservice/isviable(for:).md)
  Queries whether the device can perform RCS operations at this time.
- [var viabilityNotifications: some AsyncSequence<RCSService.ViabilityNotification, Never>](rcsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by the service.
- [RCSService.ViabilityNotification](rcsservice/viabilitynotification.md)
  A notification that indicates whether RCS is viable for a given cellular service.
### Managing RCS configuration
- [func configuration(for: CellularServiceID) throws -> RCSService.Configuration](rcsservice/configuration(for:).md)
  Retrieves the RCS configuration for the specified cellular service.
- [RCSService.Configuration](rcsservice/configuration.md)
  A structure that contains RCS configuration parameters, such as timing and size limits.
### Sending messages
- [func sendMessage(RCSMessage.Text, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-70q7h.md)
  Sends a text message to a specified destination.
- [RCSMessage.Text](rcsmessage/text.md)
  A structure that represents text content in an RCS message.
- [func sendMessage(RCSMessage.FileTransfer, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-63zct.md)
  Sends a file transfer message to a specified destination.
- [RCSMessage.FileTransfer](rcsmessage/filetransfer.md)
  A structure that represents file transfer content in an RCS message.
- [func sendMessage(RCSMessage.ComposingIndicator, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-9i178.md)
  Sends a composing indicator message to a specified destination.
- [RCSMessage.ComposingIndicator](rcsmessage/composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.
- [func sendMessage(RCSMessage.GeolocationPush, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-y1z.md)
  Sends a geolocation push message to a specified destination.
- [RCSMessage.GeolocationPush](rcsmessage/geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
- [func sendMessage(RCSMessage.DispositionNotification, to: RCSHandle.URI, using: CellularServiceID, messageID: RCSMessageID, group: RCSHandle.Group?) async throws](rcsservice/sendmessage(_:to:using:messageid:group:).md)
  Sends the disposition for an incoming message.
- [RCSMessage.DispositionNotification](rcsmessage/dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.
### Receiving messages
- [var incomingMessageNotifications: some AsyncSequence<RCSService.IncomingMessageNotification, Never>](rcsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.
- [RCSService.IncomingMessageNotification](rcsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming RCS message.
- [struct RCSMessage](rcsmessage.md)
  A structure that contains an RCS message’s content and metadata.
### Revoking messages
- [func revokeMessage(RCSService.RevokeMessageRequest) async throws -> Bool](rcsservice/revokemessage(_:).md)
  Requests revocation of an RCS message.
- [RCSService.RevokeMessageRequest](rcsservice/revokemessagerequest.md)
  A structure that respresents a request to revoke a previously sent message.
### Transferring files
- [func upload(RCSService.FileUploadRequest) async throws -> RCSService.FileUploadRequest.Metadata](rcsservice/upload(_:).md)
  Uploads a file to the RCS content server.
- [RCSService.FileUploadRequest](rcsservice/fileuploadrequest.md)
  A structure that represents an RCS file upload request.
- [RCSService.FileUploadRequest.Metadata](rcsservice/fileuploadrequest/metadata.md)
  A structure that contains upload metadata from the content server.
- [func download(RCSService.FileDownloadRequest) async throws -> RCSService.FileDownloadRequest.Metadata](rcsservice/download(_:).md)
  Downloads a file from the RCS content server.
- [RCSService.FileDownloadRequest](rcsservice/filedownloadrequest.md)
  A structure that represents an RCS file download request.
- [RCSService.FileDownloadRequest.Metadata](rcsservice/filedownloadrequest/metadata.md)
  A structure that contains download metadata from the content server.
### Receiving handle updates
- [var remoteHandleUpdates: some AsyncSequence<RCSService.RemoteHandleUpdate, Never>](rcsservice/remotehandleupdates.md)
  An asynchronous sequence of remote handle updates produced by this service.
- [RCSService.RemoteHandleUpdate](rcsservice/remotehandleupdate.md)
  A structure that contains information about an update to a remote handle.
### Reporting spam
- [func reportSpam(RCSService.ReportSpamRequest) async throws](rcsservice/reportspam(_:).md)
  Reports an RCS message as spam to the carrier and to partners.
- [RCSService.ReportSpamRequest](rcsservice/reportspamrequest.md)
  A structure that contains information about a spam reporting request for an RCS message.
### Managing group chats
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
### Discovering remote capabilities
- [func remoteCapabilities(for: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?](rcsservice/remotecapabilities(for:).md)
  Requests remote capability discovery for a given handle
- [RCSService.RemoteCapabilitiesRequest](rcsservice/remotecapabilitiesrequest.md)
  A structure representing a request to retrieve the capabilities of a remote handle.
- [RCSService.RemoteCapabilities](rcsservice/remotecapabilities.md)
  Structure representing the capabilities of a remote handle.
### Responding to business suggestions
- [func sendSuggestionResponse(RCSService.SuggestionResponse) async throws](rcsservice/sendsuggestionresponse(_:).md)
  Sends a response for a business suggestion.
- [RCSService.SuggestionResponse](rcsservice/suggestionresponse.md)
  Structure representing a response to a business suggestion.
### Retrieving business information
- [func businessInformation(for: RCSService.BusinessInformationRequest) async throws -> RCSService.Business?](rcsservice/businessinformation(for:).md)
  Requests business information for a specified handle.
- [RCSService.BusinessInformationRequest](rcsservice/businessinformationrequest.md)
  A structure representing a request to retrieve information about a business.
- [RCSService.Business](rcsservice/business.md)
  Structure containing details about a business.
### Handling errors
- [RCSService.Error](rcsservice/error.md)
  A type to define errors that can occur when performing RCS operations.
### Supporting types
- [RCSService.GroupChatEndedEvent](rcsservice/groupchatendedevent.md)
  Event triggered when a group chat is ended.
- [RCSService.GroupChatParticipantsAddedEvent](rcsservice/groupchatparticipantsaddedevent.md)
  Event triggered when participants are added to a group.
- [RCSService.GroupChatParticipantsRemovedEvent](rcsservice/groupchatparticipantsremovedevent.md)
  Event triggered when participants are removed from a group.
- [RCSService.GroupChatStartedEvent](rcsservice/groupchatstartedevent.md)
  Event triggered when group chat is started.
- [RCSService.GroupChatSubjectUpdatedEvent](rcsservice/groupchatsubjectupdatedevent.md)
  Event triggered when a group’s subject is updated.
### Instance Methods
- [func sendDeviceSpecifics(to: RCSHandle.URI, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/senddevicespecifics(to:using:messageid:).md)
  Sends device specifics in response to a suggested action to send device specifics.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var rcsService: RCSService](telephonymessagingsession/rcsservice.md)
  RCS service associated with this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice)*