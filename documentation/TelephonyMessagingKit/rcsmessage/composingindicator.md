# RCSMessage.ComposingIndicator

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents RFC 3994 composing indicator content in an RCS message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct ComposingIndicator
```

#### Overview

This content type indicates whether the party sending the message is currently active. Your app can use this to provide an “is typing” indicator to the person using the app.

## Topics

### Creating a composing indicator instance
- [init(state: RCSMessage.ComposingIndicator.State, lastActive: Date?, contentType: UTType?, refreshInterval: Duration?)](rcsmessage/composingindicator/init(state:lastactive:contenttype:refreshinterval:).md)
### Accessing composing indicator properties
- [var state: RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.property.md)
  The state of the composer.
- [RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.enum.md)
  An enumeration that represents the state of the indicator.
- [var lastActive: Date?](rcsmessage/composingindicator/lastactive.md)
  The time of last activity.
- [var contentType: UTType?](rcsmessage/composingindicator/contenttype.md)
  The type of message being composed.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [var refreshInterval: Duration?](rcsmessage/composingindicator/refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.

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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator)*