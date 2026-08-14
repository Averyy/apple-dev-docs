# MEMessageEncodingResult

**Framework**: MailKit  
**Kind**: class

An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageEncodingResult
```

## Topics

### Providing an Encoding Result
- [init(encodedMessage: MEEncodedOutgoingMessage?, signingError: (any Error)?, encryptionError: (any Error)?)](memessageencodingresult/init(encodedmessage:signingerror:encryptionerror:).md)
  Creates an encoding result object with a signed or encrypted message, or errors if the message encoder fails to encode the message.
- [var encodedMessage: MEEncodedOutgoingMessage?](memessageencodingresult/encodedmessage.md)
  A signed or encrypted message, if the message security handler needs to encode the message.
- [var encryptionError: (any Error)?](memessageencodingresult/encryptionerror.md)
  An error that occurred while the message encoder encrypted the message.
- [var signingError: (any Error)?](memessageencodingresult/signingerror.md)
  An error that occurred while the message encoder signed the message.
### Initializers
- [init?(coder: NSCoder)](memessageencodingresult/init(coder:).md)

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
- [class MEOutgoingMessageEncodingStatus](meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencodingresult)*