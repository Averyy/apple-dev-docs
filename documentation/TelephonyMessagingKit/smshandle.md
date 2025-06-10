# SMSHandle

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an SMS address.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct SMSHandle
```

## Topics

### Creating a handle
- [init(phoneNumber: String)](smshandle/init(phonenumber:).md)
  Initializes a handle instance with the given phone number.
### Accessing handle properties
- [let phoneNumber: String](smshandle/phonenumber.md)
  The phone number for this handle.
### Encoding and decoding
- [init(from: any Decoder) throws](smshandle/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](smshandle/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let cellularServiceID: CellularServiceID](smsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let handle: SMSHandle](smsmessage/handle.md)
  A handle that represents the originator of an incoming message or the destination of an outgoing message.
- [let messageID: SMSMessageID](smsmessage/messageid.md)
  A message identifier for the message.
- [struct SMSMessageID](smsmessageid.md)
  A structure that represents an SMS message identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smshandle)*