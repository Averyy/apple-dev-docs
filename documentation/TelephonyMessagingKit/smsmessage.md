# SMSMessage

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains the data of an SMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct SMSMessage
```

## Topics

### Creating an SMS message
- [init(cellularServiceID: CellularServiceID, handle: SMSHandle, messageID: SMSMessageID, content: SMSContent)](smsmessage/init(cellularserviceid:handle:messageid:content:).md)
  Initializes an SMS Message for sending to a receipient.
### Accessing message content
- [let content: SMSContent](smsmessage/content.md)
  The textual content of the message.
- [struct SMSContent](smscontent.md)
  A structure that holds the content of an SMS message.
### Accessing message properties
- [let cellularServiceID: CellularServiceID](smsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: SMSHandle](smsmessage/handle.md)
  A handle that represents the originator of an incoming message or the destination of an outgoing message.
- [struct SMSHandle](smshandle.md)
  A structure that represents an SMS address.
- [let messageID: SMSMessageID](smsmessage/messageid.md)
  A message identifier for the message.
- [struct SMSMessageID](smsmessageid.md)
  A structure that represents an SMS message identifier.
### Encoding and decoding
- [init(from: any Decoder) throws](smsmessage/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](smsmessage/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func sendMessage(SMSMessage) async throws](smsservice/sendmessage(_:).md)
  Sends an SMS message to the given destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsmessage)*