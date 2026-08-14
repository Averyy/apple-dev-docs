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
### Initializers
- [init(NDEFRecords: [NFCNDEFPayload])](nfcndefmessage/init(ndefrecords:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class NFCNDEFPayload](nfcndefpayload.md)
  A payload record in an NFC NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefmessage)*