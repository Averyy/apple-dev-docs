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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol MEMessageEncoder](memessageencoder.md)
  An object that encrypts or digitally signs outgoing messages.
- [class MEEncodedOutgoingMessage](meencodedoutgoingmessage.md)
  An object that contains the signed or encrypted representation of a message’s RFC 2822 data.
- [class MEMessageEncodingResult](memessageencodingresult.md)
  An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meoutgoingmessageencodingstatus)*