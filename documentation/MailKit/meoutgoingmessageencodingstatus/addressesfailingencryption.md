# addressesFailingEncryption

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

An array of email addresses that prevent the message security handler from signing the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var addressesFailingEncryption: [MEEmailAddress] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<MEEmailAddress *> * addressesFailingEncryption;
```

## See Also

### Providing Encoding Status
- [init(canSign: Bool, canEncrypt: Bool, securityError: (any Error)?, addressesFailingEncryption: [MEEmailAddress])](./init%28cansign,canencrypt,securityerror,addressesfailingencryption%29.md)
  Creates an object that describes whether the message security handler can encrypt or sign an outgoing message.
- [var canSign: Bool](./cansign.md)
  A Boolean value that indicates the message security handler can digitally sign the outgoing message.
- [var canEncrypt: Bool](./canencrypt.md)
  A Boolean value that indicates the message security handler can encrypt the outgoing message.
- [var securityError: (any Error)?](./securityerror.md)
  An error that the message encoder encountered while determining the encoding status for the outgoing message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meoutgoingmessageencodingstatus/addressesfailingencryption)*