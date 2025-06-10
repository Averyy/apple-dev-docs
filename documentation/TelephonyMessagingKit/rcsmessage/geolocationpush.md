# RCSMessage.GeolocationPush

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents geolocation push content in an RCS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct GeolocationPush
```

## Topics

### Accessing geolocation properties
- [let latitude: Double](rcsmessage/geolocationpush/latitude.md)
  The latitude of the location.
- [let longitude: Double](rcsmessage/geolocationpush/longitude.md)
  The longitude of the location.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsmessage/geolocationpush/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsmessage/geolocationpush/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing geolocation push instances
- [static func == (RCSMessage.GeolocationPush, RCSMessage.GeolocationPush) -> Bool](rcsmessage/geolocationpush/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(latitude: Double, longitude: Double, description: String?)](rcsmessage/geolocationpush/init(latitude:longitude:description:).md)
  Creates a geolocation push content instance with the given latitude and longitude.
### Instance Properties
- [let description: String?](rcsmessage/geolocationpush/description.md)
  A textual description of the location.
### Default Implementations
- [Equatable Implementations](rcsmessage/geolocationpush/equatable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/geolocationpush)*