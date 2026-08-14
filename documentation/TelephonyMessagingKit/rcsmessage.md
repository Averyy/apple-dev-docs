# RCSMessage

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains an RCS message’s content and metadata.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RCSMessage
```

#### Overview

When handling received messages, use the [`content`](rcsmessage/content-swift.property.md) property to distinguish between different types of messages, such as [`RCSMessage.Text`](rcsmessage/text.md) or [`RCSMessage.DispositionNotification`](rcsmessage/dispositionnotification.md).

## Topics

### Accessing message content
- [let content: RCSMessage.Content](rcsmessage/content-swift.property.md)
  The content of the message.
- [RCSMessage.Content](rcsmessage/content-swift.enum.md)
  An enumeration of the RCS message content types supported by the system.
### Working with content types
- [RCSMessage.Text](rcsmessage/text.md)
  A structure that represents text content in an RCS message.
- [RCSMessage.FileTransfer](rcsmessage/filetransfer.md)
  A structure that represents file transfer content in an RCS message.
- [RCSMessage.GeolocationPush](rcsmessage/geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
- [RCSMessage.DispositionNotification](rcsmessage/dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [RCSMessage.Disposition](rcsmessage/disposition.md)
  An enumeration that represents the disposition of an RCS message, such as whether delivery succeeded or failed.
- [RCSMessage.ComposingIndicator](rcsmessage/composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.
### Accessing message properties
- [let cellularServiceID: CellularServiceID](rcsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: RCSHandle](rcsmessage/handle.md)
  The handle associated with the sender or receiver of the message.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [let id: RCSMessageID](rcsmessage/id.md)
  A message identifier for the message.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.
- [let originalID: RCSMessageID?](rcsmessage/originalid.md)
  The original message ID of this message.
### Supporting types
- [RCSMessage.SecureSendReceipt](rcsmessage/securesendreceipt.md)
  A structure that contains the security context of an end-to-end encrypted message.
### Structures
- [RCSMessage.CustomReaction](rcsmessage/customreaction.md)
  A structure that represents a custom reaction to an RCS message.
- [RCSMessage.Reaction](rcsmessage/reaction.md)
  A structure that represents a reaction to an RCS message.
- [RCSMessage.Reply](rcsmessage/reply.md)
  A structure that represents a reply to an RCS message.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var incomingMessageNotifications: some AsyncSequence<RCSService.IncomingMessageNotification, Never>](rcsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.
- [RCSService.IncomingMessageNotification](rcsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage)*