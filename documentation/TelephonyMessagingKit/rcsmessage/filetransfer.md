# RCSMessage.FileTransfer

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents file transfer content in an RCS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct FileTransfer
```

#### Overview

When sending a file to a recipient, you use the [`RCSService`](../rcsservice.md) to call [`upload(_:)`](../rcsservice/upload%28_%29.md) and use the metadata returned by that method to create a message of this type. When receiving a file, you handle messages of this type in the [`incomingMessageNotifications`](../rcsservice/incomingmessagenotifications.md) asynchronous sequence, and use the received message to create a [`RCSService.FileDownloadRequest`](../rcsservice/filedownloadrequest.md) for use with [`download(_:)`](../rcsservice/download%28_%29.md).

## Topics

### Creating a file transfer instance
- [init(fileMetadata: RCSFileTransferMetadata, thumbnailMetadata: RCSFileTransferMetadata?)](./filetransfer/init%28filemetadata,thumbnailmetadata%29.md)
  Creates a file transfer content instance with the given metadata.
- [struct RCSFileTransferMetadata](../rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.
### Accessing file transfer properties
- [var fileMetadata: RCSFileTransferMetadata](./filetransfer/filemetadata.md)
  Metadata for the transferred file.
- [var thumbnailMetadata: RCSFileTransferMetadata?](./filetransfer/thumbnailmetadata.md)
  Metadata for the transferred thumbnail.
### Supporting RCS encryption
- [var isEndToEndEncrypted: Bool](./filetransfer/isendtoendencrypted.md)
  A Boolean value indicating whether this message is end-to-end encrypted.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending messages
- [func sendMessage(RCSMessage.Text, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](../rcsservice/sendmessage%28_,to,using,messageid%29-70q7h.md)
  Sends a text message to a specified destination.
- [RCSMessage.Text](./text.md)
  A structure that represents text content in an RCS message.
- [func sendMessage(RCSMessage.FileTransfer, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](../rcsservice/sendmessage%28_,to,using,messageid%29-63zct.md)
  Sends a file transfer message to a specified destination.
- [func sendMessage(RCSMessage.ComposingIndicator, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](../rcsservice/sendmessage%28_,to,using,messageid%29-9i178.md)
  Sends a composing indicator message to a specified destination.
- [RCSMessage.ComposingIndicator](./composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.
- [func sendMessage(RCSMessage.GeolocationPush, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](../rcsservice/sendmessage%28_,to,using,messageid%29-y1z.md)
  Sends a geolocation push message to a specified destination.
- [RCSMessage.GeolocationPush](./geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
- [func sendMessage(RCSMessage.DispositionNotification, to: RCSHandle.URI, using: CellularServiceID, messageID: RCSMessageID, group: RCSHandle.Group?) async throws](../rcsservice/sendmessage%28_,to,using,messageid,group%29.md)
  Sends the disposition for an incoming message.
- [RCSMessage.DispositionNotification](./dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [enum RCSHandle](../rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [struct CellularServiceID](../cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct RCSMessageID](../rcsmessageid.md)
  A structure that represents an RCS message identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/filetransfer)*