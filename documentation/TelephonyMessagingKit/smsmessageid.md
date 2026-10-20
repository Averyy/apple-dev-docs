# SMSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an SMS message identifier.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct SMSMessageID
```

## Topics

### Creating a message ID
- [init(rawValue: UInt32)](./smsmessageid/init%28rawvalue%29.md)
  Initializes an message identifier with the given rawValue.
### Describing a message ID
- [var description: String](./smsmessageid/description.md)
  A textual representation of the identifier.
### Working with raw values
- [let rawValue: UInt32](./smsmessageid/rawvalue.md)
  The identifier of an SMS message.

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

### Accessing message properties
- [let cellularServiceID: CellularServiceID](./smsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](./cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: SMSHandle](./smsmessage/handle.md)
  A handle that represents the originator of an incoming message or the destination of an outgoing message.
- [struct SMSHandle](./smshandle.md)
  A structure that represents an SMS address.
- [let messageID: SMSMessageID](./smsmessage/messageid.md)
  A message identifier for the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsmessageid)*