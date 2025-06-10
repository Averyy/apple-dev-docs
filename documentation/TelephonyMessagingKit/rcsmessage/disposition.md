# RCSMessage.Disposition

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the disposition of an RCS message, such as whether delivery succeeded or failed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Disposition
```

## Topics

### Accessing disposition values
- [RCSMessage.Disposition.delivered](rcsmessage/disposition/delivered.md)
  The carrier delivered the message.
- [RCSMessage.Disposition.deliveryFailed](rcsmessage/disposition/deliveryfailed.md)
  The carrier failed to deliver the message.
- [RCSMessage.Disposition.displayed](rcsmessage/disposition/displayed.md)
  The recipient device displayed the message.
- [RCSMessage.Disposition.interworkingDelivered](rcsmessage/disposition/interworkingdelivered.md)
  The carrier used a non-CPM technology to deliver the message.
- [RCSMessage.Disposition.interworkingFailed](rcsmessage/disposition/interworkingfailed.md)
  The carrier attempted to use a non-CPM technology to deliver the message, but failed.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsmessage/disposition/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSMessage.Disposition, RCSMessage.Disposition) -> Bool](rcsmessage/disposition/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsmessage/disposition/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsmessage/disposition/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsmessage/disposition/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsmessage/disposition/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [RCSMessage.Text](rcsmessage/text.md)
  A structure that represents text content in an RCS message.
- [RCSMessage.FileTransfer](rcsmessage/filetransfer.md)
  A structure that represents file transfer content in an RCS message.
- [RCSMessage.GeolocationPush](rcsmessage/geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
- [RCSMessage.DispositionNotification](rcsmessage/dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [RCSMessage.ComposingIndicator](rcsmessage/composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/disposition)*