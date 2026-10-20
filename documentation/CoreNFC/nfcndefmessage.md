# NFCNDEFMessage

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

An NFC NDEF message consisting of an array of payload records.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCNDEFMessage
```

```objc
@interface NFCNDEFMessage : NSObject
```

## Topics

### Creating an NDEF Message
- [init(records: [NFCNDEFPayload])](./nfcndefmessage/init%28records%29.md)
  Creates an NDEF message with the specified records.
- [convenience init?(data: Data)](./nfcndefmessage/init%28data%29.md)
  Creates an NDEF message from raw data representing the message.
### Accessing NDEF Records
- [var records: [NFCNDEFPayload]](./nfcndefmessage/records.md)
  An array of records for the message.
### Getting the Message Length
- [var length: Int](./nfcndefmessage/length.md)
  The length, in bytes, of the NDEF message when stored on an NFC tag.
### Initializers
- [init(NDEFRecords: [NFCNDEFPayload])](./nfcndefmessage/init%28ndefrecords%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### NDEF messages and payloads
- [class NFCNDEFPayload](./nfcndefpayload.md)
  A payload record in an NFC NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefmessage)*