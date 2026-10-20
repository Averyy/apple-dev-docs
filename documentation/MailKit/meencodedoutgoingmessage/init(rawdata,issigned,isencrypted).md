# init(rawData:isSigned:isEncrypted:)

**Framework**: MailKit  
**Kind**: init  
**Role**: Initializer

Creates an object that contains the outgoing message’s encoded data, and indicates if the encoder encrypted or signed the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(rawData: Data, isSigned: Bool, isEncrypted: Bool)
```

```objc
- (instancetype) initWithRawData:(NSData *) rawData isSigned:(BOOL) isSigned isEncrypted:(BOOL) isEncrypted;
```

## Parameters

- `rawData`: The encrypted, signed, or both encrypted and signed message data.
- `isSigned`: A Boolean value that indicates if the data contains a signed message.
- `isEncrypted`: A Boolean value that indicates if the data contains an encrypted message.

## See Also

### Encoding Outgoing Messages
- [var isEncrypted: Bool](./isencrypted.md)
  A Boolean value that indicates if the message encoder encrypted the message.
- [var isSigned: Bool](./issigned.md)
  A Boolean value that indicates if the message encoder signed the message.
- [var rawData: Data](./rawdata.md)
  The encrypted, signed, or both encrypted and signed data for the outgoing message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meencodedoutgoingmessage/init(rawdata:issigned:isencrypted:))*