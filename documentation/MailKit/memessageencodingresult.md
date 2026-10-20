# MEMessageEncodingResult

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageEncodingResult
```

```objc
@interface MEMessageEncodingResult : NSObject
```

## Topics

### Providing an Encoding Result
- [init(encodedMessage: MEEncodedOutgoingMessage?, signingError: (any Error)?, encryptionError: (any Error)?)](./memessageencodingresult/init%28encodedmessage,signingerror,encryptionerror%29.md)
  Creates an encoding result object with a signed or encrypted message, or errors if the message encoder fails to encode the message.
- [var encodedMessage: MEEncodedOutgoingMessage?](./memessageencodingresult/encodedmessage.md)
  A signed or encrypted message, if the message security handler needs to encode the message.
- [var encryptionError: (any Error)?](./memessageencodingresult/encryptionerror.md)
  An error that occurred while the message encoder encrypted the message.
- [var signingError: (any Error)?](./memessageencodingresult/signingerror.md)
  An error that occurred while the message encoder signed the message.
### Initializers
- [init?(coder: NSCoder)](./memessageencodingresult/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Encrypting and Signing Messages
- [protocol MEMessageEncoder](./memessageencoder.md)
  An object that encrypts or digitally signs outgoing messages.
- [class MEEncodedOutgoingMessage](./meencodedoutgoingmessage.md)
  An object that contains the signed or encrypted representation of a message’s RFC 2822 data.
- [class MEOutgoingMessageEncodingStatus](./meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencodingresult)*