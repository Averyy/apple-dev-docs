# RCSMessage

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains an RCS message’s content and metadata.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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
- [let id: RCSMessageID](rcsmessage/id-swift.property.md)
  A message identifier for the message.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsmessage/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSMessage, RCSMessage) -> Bool](rcsmessage/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsmessage/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [RCSMessage.ID](rcsmessage/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](rcsmessage/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var incomingMessageNotifications: some AsyncSequence<RCSService.IncomingMessageNotification, Never>](rcsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.
- [RCSService.IncomingMessageNotification](rcsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage)*