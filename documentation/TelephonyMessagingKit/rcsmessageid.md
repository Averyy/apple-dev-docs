# RCSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an RCS message identifier.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RCSMessageID
```

## Topics

### Describing a message ID
- [var description: String](./rcsmessageid/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sending messages
- [func sendMessage(RCSMessage.Text, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](./rcsservice/sendmessage%28_,to,using,messageid%29-70q7h.md)
  Sends a text message to a specified destination.
- [RCSMessage.Text](./rcsmessage/text.md)
  A structure that represents text content in an RCS message.
- [func sendMessage(RCSMessage.FileTransfer, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](./rcsservice/sendmessage%28_,to,using,messageid%29-63zct.md)
  Sends a file transfer message to a specified destination.
- [RCSMessage.FileTransfer](./rcsmessage/filetransfer.md)
  A structure that represents file transfer content in an RCS message.
- [func sendMessage(RCSMessage.ComposingIndicator, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](./rcsservice/sendmessage%28_,to,using,messageid%29-9i178.md)
  Sends a composing indicator message to a specified destination.
- [RCSMessage.ComposingIndicator](./rcsmessage/composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.
- [func sendMessage(RCSMessage.GeolocationPush, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](./rcsservice/sendmessage%28_,to,using,messageid%29-y1z.md)
  Sends a geolocation push message to a specified destination.
- [RCSMessage.GeolocationPush](./rcsmessage/geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
- [func sendMessage(RCSMessage.DispositionNotification, to: RCSHandle.URI, using: CellularServiceID, messageID: RCSMessageID, group: RCSHandle.Group?) async throws](./rcsservice/sendmessage%28_,to,using,messageid,group%29.md)
  Sends the disposition for an incoming message.
- [RCSMessage.DispositionNotification](./rcsmessage/dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [enum RCSHandle](./rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [struct CellularServiceID](./cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessageid)*