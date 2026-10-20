# MMSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an MMS message identifier.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct MMSMessageID
```

## Topics

### Creating a message ID
- [init(rawValue: UInt32)](./mmsmessageid/init%28rawvalue%29.md)
  Initializes an message identifier with the given raw value.
### Describing a message ID
- [var description: String](./mmsmessageid/description.md)
  A textual representation of the identifier.
### Working with raw values
- [let rawValue: UInt32](./mmsmessageid/rawvalue.md)
  The identifier of an MMS message.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Receiving messages
- [struct CellularServiceID](./cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](./mmsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.
- [MMSService.IncomingMessageNotification](./mmsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsmessageid)*