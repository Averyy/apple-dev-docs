# securityError

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

An error that the message encoder encountered while determining the encoding status for the outgoing message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var securityError: (any Error)? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSError * securityError;
```

## See Also

### Providing Encoding Status
- [init(canSign: Bool, canEncrypt: Bool, securityError: (any Error)?, addressesFailingEncryption: [MEEmailAddress])](./init%28cansign,canencrypt,securityerror,addressesfailingencryption%29.md)
  Creates an object that describes whether the message security handler can encrypt or sign an outgoing message.
- [var canSign: Bool](./cansign.md)
  A Boolean value that indicates the message security handler can digitally sign the outgoing message.
- [var canEncrypt: Bool](./canencrypt.md)
  A Boolean value that indicates the message security handler can encrypt the outgoing message.
- [var addressesFailingEncryption: [MEEmailAddress]](./addressesfailingencryption.md)
  An array of email addresses that prevent the message security handler from signing the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meoutgoingmessageencodingstatus/securityerror)*