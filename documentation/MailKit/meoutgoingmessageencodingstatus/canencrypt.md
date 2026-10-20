# canEncrypt

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the message security handler can encrypt the outgoing message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var canEncrypt: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL canEncrypt;
```

## See Also

### Providing Encoding Status
- [init(canSign: Bool, canEncrypt: Bool, securityError: (any Error)?, addressesFailingEncryption: [MEEmailAddress])](./init%28cansign,canencrypt,securityerror,addressesfailingencryption%29.md)
  Creates an object that describes whether the message security handler can encrypt or sign an outgoing message.
- [var canSign: Bool](./cansign.md)
  A Boolean value that indicates the message security handler can digitally sign the outgoing message.
- [var securityError: (any Error)?](./securityerror.md)
  An error that the message encoder encountered while determining the encoding status for the outgoing message.
- [var addressesFailingEncryption: [MEEmailAddress]](./addressesfailingencryption.md)
  An array of email addresses that prevent the message security handler from signing the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meoutgoingmessageencodingstatus/canencrypt)*