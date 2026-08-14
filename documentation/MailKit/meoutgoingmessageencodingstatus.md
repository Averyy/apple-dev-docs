# MEOutgoingMessageEncodingStatus

**Framework**: MailKit  
**Kind**: class

An object that contains information about security measures the user can apply when composing a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEOutgoingMessageEncodingStatus
```

#### Overview

As a user composes a new message, MailKit requests the encoding status from your message security handler. The handler provides an [`MEOutgoingMessageEncodingStatus`](meoutgoingmessageencodingstatus.md) that contains:

- Boolean values that indicate if the handler can sign or encrypt the message
- An error if verifying the security status fails
- An array of recipient addresses for which the handler can’t encrypt the message

## Topics

### Providing Encoding Status
- [init(canSign: Bool, canEncrypt: Bool, securityError: (any Error)?, addressesFailingEncryption: [MEEmailAddress])](meoutgoingmessageencodingstatus/init(cansign:canencrypt:securityerror:addressesfailingencryption:).md)
  Creates an object that describes whether the message security handler can encrypt or sign an outgoing message.
- [var canSign: Bool](meoutgoingmessageencodingstatus/cansign.md)
  A Boolean value that indicates the message security handler can digitally sign the outgoing message.
- [var canEncrypt: Bool](meoutgoingmessageencodingstatus/canencrypt.md)
  A Boolean value that indicates the message security handler can encrypt the outgoing message.
- [var securityError: (any Error)?](meoutgoingmessageencodingstatus/securityerror.md)
  An error that the message encoder encountered while determining the encoding status for the outgoing message.
- [var addressesFailingEncryption: [MEEmailAddress]](meoutgoingmessageencodingstatus/addressesfailingencryption.md)
  An array of email addresses that prevent the message security handler from signing the message.
### Initializers
- [init?(coder: NSCoder)](meoutgoingmessageencodingstatus/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [protocol MEMessageEncoder](memessageencoder.md)
  An object that encrypts or digitally signs outgoing messages.
- [class MEEncodedOutgoingMessage](meencodedoutgoingmessage.md)
  An object that contains the signed or encrypted representation of a message’s RFC 2822 data.
- [class MEMessageEncodingResult](memessageencodingresult.md)
  An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meoutgoingmessageencodingstatus)*