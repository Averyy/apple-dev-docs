# SMSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an SMS message identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct SMSMessageID
```

## Topics

### Creating a message ID
- [init(rawValue: UInt32)](smsmessageid/init(rawvalue:).md)
  Initializes an message identifier with the given rawValue.
### Describing a message ID
- [var description: String](smsmessageid/description.md)
  A textual representation of the identifier.
### Working with raw values
- [let rawValue: UInt32](smsmessageid/rawvalue-swift.property.md)
  The identifier of an SMS message.
- [SMSMessageID.RawValue](smsmessageid/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](smsmessageid/equatable-implementations.md)
- [RawRepresentable Implementations](smsmessageid/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsmessageid)*