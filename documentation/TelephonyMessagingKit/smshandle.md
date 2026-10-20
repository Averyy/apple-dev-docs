# SMSHandle

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an SMS address.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct SMSHandle
```

## Mentions

- [Creating a carrier messaging app](./creating-a-carrier-messaging-app.md)

## Topics

### Creating a handle
- [init(phoneNumber: String)](./smshandle/init%28phonenumber%29.md)
  Initializes a handle instance with the given phone number.
### Accessing handle properties
- [let phoneNumber: String](./smshandle/phonenumber.md)
  The phone number for this handle.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
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
- [let messageID: SMSMessageID](./smsmessage/messageid.md)
  A message identifier for the message.
- [struct SMSMessageID](./smsmessageid.md)
  A structure that represents an SMS message identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smshandle)*