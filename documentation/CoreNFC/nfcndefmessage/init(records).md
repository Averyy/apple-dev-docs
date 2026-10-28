# init(records:)

**Framework**: Core NFC  
**Kind**: init  
**Role**: Initializer

Creates an NDEF message with the specified records.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(records: [NFCNDEFPayload])
```

```objc
- (instancetype) initWithNDEFRecords:(NSArray<NFCNDEFPayload *> *) records;
```

## Return Value

A newly initialized NDEF message object.

## Parameters

- `records`: An array of payload objects for the message. To create an empty message, pass in an empty array.

## See Also

### Creating an NDEF Message
- [convenience init?(data: Data)](./init%28data%29.md)
  Creates an NDEF message from raw data representing the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefmessage/init(records:))*