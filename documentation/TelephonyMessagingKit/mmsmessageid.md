# MMSMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an MMS message identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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
- [let rawValue: UInt32](mmsmessageid/rawvalue-swift.property.md)
  The identifier of an MMS message.
- [MMSMessageID.RawValue](mmsmessageid/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](mmsmessageid/equatable-implementations.md)
- [RawRepresentable Implementations](mmsmessageid/rawrepresentable-implementations.md)

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

- [func receiveMessage(using: CellularServiceID, messageID: MMSMessageID) async throws -> MMSMessage](mmsservice/receivemessage(using:messageid:).md)
  Retrieves an MMS message that matches the given identifiers.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](mmsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.
- [MMSService.IncomingMessageNotification](mmsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming MMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsmessageid)*