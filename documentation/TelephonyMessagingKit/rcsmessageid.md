# RCSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an RCS message identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct RCSMessageID
```

## Topics

### Describing a message ID
- [var description: String](rcsmessageid/description.md)
  A textual representation of this instance.
### Working with raw values
- [init(rawValue: String)](rcsmessageid/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [let rawValue: String](rcsmessageid/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [RCSMessageID.RawValue](rcsmessageid/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](rcsmessageid/equatable-implementations.md)
- [RawRepresentable Implementations](rcsmessageid/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [RCSMessage.DispositionNotification](rcsmessage/dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessageid)*