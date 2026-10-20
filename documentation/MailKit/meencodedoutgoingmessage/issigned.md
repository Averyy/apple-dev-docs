# isSigned

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the message encoder signed the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var isSigned: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isSigned;
```

## See Also

### Encoding Outgoing Messages
- [init(rawData: Data, isSigned: Bool, isEncrypted: Bool)](./init%28rawdata,issigned,isencrypted%29.md)
  Creates an object that contains the outgoing message’s encoded data, and indicates if the encoder encrypted or signed the message.
- [var isEncrypted: Bool](./isencrypted.md)
  A Boolean value that indicates if the message encoder encrypted the message.
- [var rawData: Data](./rawdata.md)
  The encrypted, signed, or both encrypted and signed data for the outgoing message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meencodedoutgoingmessage/issigned)*