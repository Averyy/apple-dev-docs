# MMSMessage

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains the data of an MMS message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct MMSMessage
```

## Topics

### Creating an MMS message
- [init(cellularServiceID: CellularServiceID, messageID: MMSMessageID, content: MMSContent)](mmsmessage/init(cellularserviceid:messageid:content:).md)
  Initializes an MMS message for sending to a receipient.
### Accessing message content
- [var content: MMSContent](mmsmessage/content.md)
  The body content of the message.
- [struct MMSContent](mmscontent.md)
  A structure that holds the content of an MMS message.
### Accessing message properties
- [var cellularServiceID: CellularServiceID](mmsmessage/cellularserviceid.md)
  The cellular service identifier associated with the message.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [var messageID: MMSMessageID](mmsmessage/messageid.md)
  A message identifier for the message.
- [struct MMSMessageID](mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [var totalSize: Measurement<UnitInformationStorage>](mmsmessage/totalsize.md)
  The total size of the message.
- [var description: String](mmsmessage/description.md)
  A textual representation of the message.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func sendMessage(MMSMessage) async throws](mmsservice/sendmessage(_:).md)
  Sends an MMS message to the given destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsmessage)*