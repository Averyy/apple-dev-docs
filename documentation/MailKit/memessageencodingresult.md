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
- [class MEOutgoingMessageEncodingStatus](meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencodingresult)*