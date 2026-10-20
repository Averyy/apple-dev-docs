# RCSMessage.Disposition

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents the disposition of an RCS message, such as whether delivery succeeded or failed.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Disposition
```

## Topics

### Accessing disposition values
- [RCSMessage.Disposition.delivered](./disposition/delivered.md)
  The carrier delivered the message.
- [RCSMessage.Disposition.deliveryFailed](./disposition/deliveryfailed.md)
  The carrier failed to deliver the message.
- [RCSMessage.Disposition.displayed](./disposition/displayed.md)
  The recipient device displayed the message.
- [RCSMessage.Disposition.interworkingDelivered](./disposition/interworkingdelivered.md)
  The carrier used a non-CPM technology to deliver the message.
- [RCSMessage.Disposition.interworkingFailed](./disposition/interworkingfailed.md)
  The carrier attempted to use a non-CPM technology to deliver the message, but failed.
- [RCSMessage.Disposition.deliveryFailedDueToDecryptionFailure](./disposition/deliveryfailedduetodecryptionfailure.md)
  The recipient device was unable to decrypt the encrypted message.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with content types
- [RCSMessage.Text](./text.md)
  A structure that represents text content in an RCS message.
- [RCSMessage.FileTransfer](./filetransfer.md)
  A structure that represents file transfer content in an RCS message.
- [RCSMessage.GeolocationPush](./geolocationpush.md)
  A structure that represents geolocation push content in an RCS message.
- [RCSMessage.DispositionNotification](./dispositionnotification.md)
  A structure that represents disposition notification content in an RCS message, such as whether delivery succeeded or failed.
- [RCSMessage.ComposingIndicator](./composingindicator.md)
  A structure that represents RFC 3994 composing indicator content in an RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/disposition)*