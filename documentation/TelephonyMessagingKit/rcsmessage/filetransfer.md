# RCSMessage.FileTransfer

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents file transfer content in an RCS message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct FileTransfer
```

#### Overview

When sending a file to a recipient, you use the [`RCSService`](rcsservice.md) to call [`upload(_:)`](rcsservice/upload(_:).md) and use the metadata returned by that method to create a message of this type. When receiving a file, you handle messages of this type in the [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md) asynchronous sequence, and use the received message to create a [`RCSService.FileDownloadRequest`](rcsservice/filedownloadrequest.md) for use with [`download(_:)`](rcsservice/download(_:).md).

## Topics

### Creating a file transfer instance
- [init(fileMetadata: RCSFileTransferMetadata, thumbnailMetadata: RCSFileTransferMetadata?)](rcsmessage/filetransfer/init(filemetadata:thumbnailmetadata:).md)
  Creates a file transfer content instance with the given metadata.
- [struct RCSFileTransferMetadata](rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.
### Accessing file transfer properties
- [var fileMetadata: RCSFileTransferMetadata](rcsmessage/filetransfer/filemetadata.md)
  Metadata for the transferred file.
- [var thumbnailMetadata: RCSFileTransferMetadata?](rcsmessage/filetransfer/thumbnailmetadata.md)
  Metadata for the transferred thumbnail.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func sendMessage(RCSMessage.Text, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-70q7h.md)
  Sends a text message to a specified destination.
- [RCSMessage.Text](rcsmessage/text.md)
  A structure that represents text content in an RCS message.
- [func sendMessage(RCSMessage.FileTransfer, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-63zct.md)
  Sends a file transfer message to a specified destination.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/filetransfer)*