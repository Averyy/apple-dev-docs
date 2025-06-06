# rawData

**Framework**: MailKit  
**Kind**: property

The encrypted, signed, or both encrypted and signed data for the outgoing message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var rawData: Data { get }
```

## See Also

- [init(rawData: Data, isSigned: Bool, isEncrypted: Bool)](meencodedoutgoingmessage/init(rawdata:issigned:isencrypted:).md)
  Creates an object that contains the outgoing message’s encoded data, and indicates if the encoder encrypted or signed the message.
- [var isEncrypted: Bool](meencodedoutgoingmessage/isencrypted.md)
  A Boolean value that indicates if the message encoder encrypted the message.
- [var isSigned: Bool](meencodedoutgoingmessage/issigned.md)
  A Boolean value that indicates if the message encoder signed the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meencodedoutgoingmessage/rawdata)*