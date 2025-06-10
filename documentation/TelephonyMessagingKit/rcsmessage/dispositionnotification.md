# RCSMessage.DispositionNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct DispositionNotification
```

## Topics

### Creating a disposition notification instance
- [init(disposition: RCSMessage.Disposition, disposedMessageID: RCSMessageID)](rcsmessage/dispositionnotification/init(disposition:disposedmessageid:).md)
  Creates a disposition notification content instance with the given disposition and a message identifier.
### Accessing disposition notification properties
- [let disposition: RCSMessage.Disposition](rcsmessage/dispositionnotification/disposition.md)
  The disposition of a message.
- [RCSMessage.Disposition](rcsmessage/disposition.md)
  An enumeration that represents the disposition of an RCS message, such as whether delivery succeeded or failed.
- [let disposedMessageID: RCSMessageID](rcsmessage/dispositionnotification/disposedmessageid.md)
  The message identifier of the message.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsmessage/dispositionnotification/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsmessage/dispositionnotification/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing disposition notifications
- [static func == (RCSMessage.DispositionNotification, RCSMessage.DispositionNotification) -> Bool](rcsmessage/dispositionnotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsmessage/dispositionnotification/equatable-implementations.md)

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
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/dispositionnotification)*