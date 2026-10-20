# RCSMessage.ComposingIndicator

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents RFC 3994 composing indicator content in an RCS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct ComposingIndicator
```

#### Overview

This content type indicates whether the party sending the message is currently active. Your app can use this to provide an “is typing” indicator to the person using the app.

## Topics

### Creating a composing indicator instance
- [init(state: RCSMessage.ComposingIndicator.State, lastActive: Date?, contentType: UTType?, refreshInterval: Duration?)](./composingindicator/init%28state,lastactive,contenttype,refreshinterval%29.md)
### Accessing composing indicator properties
- [var state: RCSMessage.ComposingIndicator.State](./composingindicator/state-swift.property.md)
  The state of the composer.
- [RCSMessage.ComposingIndicator.State](./composingindicator/state-swift.enum.md)
  An enumeration that represents the state of the indicator.
- [var lastActive: Date?](./composingindicator/lastactive.md)
  The time of last activity.
- [var contentType: UTType?](./composingindicator/contenttype.md)
  The type of message being composed.
- [struct UTType](../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [var refreshInterval: Duration?](./composingindicator/refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.
### Supporting RCS encryption
- [var isEndToEndEncrypted: Bool](./composingindicator/isendtoendencrypted.md)
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
- [RCSMessage.FileTransfer](./filetransfer.md)
  A structure that represents file transfer content in an RCS message.
- [func sendMessage(RCSMessage.ComposingIndicator, to: RCSHandle, using: CellularServiceID, messageID: RCSMessageID) async throws](../rcsservice/sendmessage%28_,to,using,messageid%29-9i178.md)
  Sends a composing indicator message to a specified destination.
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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator)*