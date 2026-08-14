# MMSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an MMS message identifier.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct MMSMessageID
```

## Topics

### Creating a message ID
- [init(rawValue: UInt32)](mmsmessageid/init(rawvalue:).md)
  Initializes an message identifier with the given raw value.
### Describing a message ID
- [var description: String](mmsmessageid/description.md)
  A textual representation of the identifier.
### Working with raw values
- [let rawValue: UInt32](mmsmessageid/rawvalue.md)
  The identifier of an MMS message.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](mmsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.
- [MMSService.IncomingMessageNotification](mmsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsmessageid)*