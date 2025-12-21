# RCSMessage.Disposition

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the disposition of an RCS message, such as whether delivery succeeded or failed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
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