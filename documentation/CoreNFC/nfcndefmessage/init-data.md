# init(data:)

**Framework**: Core NFC  
**Kind**: init

Creates an NDEF message from raw data representing the message.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
convenience init?(data: Data)
```

#### Return Value

An NDEF message, or `nil` when the raw data is invalid.

## Parameters

- `data`: A data object containing the raw bytes of a complete NDEF message. The data must contain only one NDEF message, and the message must contain NDEF payloads that are valid according to the NFC Forum NDEF RTD specification.

## See Also

- [init(records: [NFCNDEFPayload])](nfcndefmessage/init(records:).md)
  Creates an NDEF message with the specified records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefmessage/init(data:))*