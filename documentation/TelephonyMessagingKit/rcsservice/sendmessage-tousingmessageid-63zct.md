# sendMessage(_:to:using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends a file transfer message to a specified destination.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func sendMessage(_ content: RCSMessage.FileTransfer, to destination: RCSHandle, using cellularServiceID: CellularServiceID, messageID: RCSMessageID) async throws
```

#### Discussion

Use this version of the `sendMessage` method in combination with the [`upload(_:)`](rcsservice/upload(_:).md) and [`download(_:)`](rcsservice/download(_:).md) methods of `RCSService`.

To send a file to a recipient, call the upload method and use the returned metadata to create a new [`RCSMessage`](rcsmessage.md) with content that’s an instance of [`RCSMessage.FileTransfer`](rcsmessage/filetransfer.md).

To receive a file, start by iterating over items in the [`incomingMessageNotifications`](rcsservice/incomingmessagenotifications.md) asynchronous sequence. When you get a message with a content value that’s [`RCSMessage.Content.fileTransfer(_:)`](rcsmessage/content-swift.enum/filetransfer(_:).md), use the file URL and other metadata in the associated [`RCSMessage.FileTransfer`](rcsmessage/filetransfer.md) value to call the download method.

## Parameters

- `content`: The content of the message to send, as an instance of  .
- `destination`: The destination handle to send the message to.
- `cellularServiceID`: The service identifier to use for the message.
- `messageID`: The message identifier to use for the message.

## See Also

- [func sendMessage(RCSMessage.Text, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/sendmessage(_:to:using:messageid:)-70q7h.md)
  Sends a text message to a specified destination.
- [RCSMessage.Text](rcsmessage/text.md)
  A structure that represents text content in an RCS message.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendmessage(_:to:using:messageid:)-63zct)*