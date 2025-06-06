# init(canSign:canEncrypt:securityError:addressesFailingEncryption:)

**Framework**: MailKit  
**Kind**: init

Creates an object that describes whether the message security handler can encrypt or sign an outgoing message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(canSign: Bool, canEncrypt: Bool, securityError: (any Error)?, addressesFailingEncryption: [MEEmailAddress])
```

## Parameters

- `canSign`: A Boolean value that indicates the message security handler can digitally sign the outgoing message.
- `canEncrypt`: A Boolean value that indicates the message security handler can encrypt the outgoing message.
- `securityError`: An error that indicates a failure while determining the encoding status for the outgoing message.
- `addressesFailingEncryption`: An array of email addresses that prevent the message security handler from signing the message.

## See Also

- [var canSign: Bool](meoutgoingmessageencodingstatus/cansign.md)
  A Boolean value that indicates the message security handler can digitally sign the outgoing message.
- [var canEncrypt: Bool](meoutgoingmessageencodingstatus/canencrypt.md)
  A Boolean value that indicates the message security handler can encrypt the outgoing message.
- [var securityError: (any Error)?](meoutgoingmessageencodingstatus/securityerror.md)
  An error that the message encoder encountered while determining the encoding status for the outgoing message.
- [var addressesFailingEncryption: [MEEmailAddress]](meoutgoingmessageencodingstatus/addressesfailingencryption.md)
  An array of email addresses that prevent the message security handler from signing the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meoutgoingmessageencodingstatus/init(cansign:canencrypt:securityerror:addressesfailingencryption:))*