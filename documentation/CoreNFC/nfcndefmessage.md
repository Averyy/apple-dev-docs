# NFCNDEFMessage

**Framework**: Core NFC  
**Kind**: class

An NFC NDEF message consisting of an array of payload records.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCNDEFMessage
```

## Topics

### Creating an NDEF Message
- [init(records: [NFCNDEFPayload])](nfcndefmessage/init(records:).md)
  Creates an NDEF message with the specified records.
- [convenience init?(data: Data)](nfcndefmessage/init(data:).md)
  Creates an NDEF message from raw data representing the message.
### Accessing NDEF Records
- [var records: [NFCNDEFPayload]](nfcndefmessage/records.md)
  An array of records for the message.
### Getting the Message Length
- [var length: Int](nfcndefmessage/length.md)
  The length, in bytes, of the NDEF message when stored on an NFC tag.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NFCNDEFPayload](nfcndefpayload.md)
  A payload record in an NFC NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefmessage)*