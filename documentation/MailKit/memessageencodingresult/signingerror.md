# signingError

**Framework**: MailKit  
**Kind**: property

An error that occurred while the message encoder signed the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var signingError: (any Error)? { get }
```

## See Also

- [init(encodedMessage: MEEncodedOutgoingMessage?, signingError: (any Error)?, encryptionError: (any Error)?)](memessageencodingresult/init(encodedmessage:signingerror:encryptionerror:).md)
  Creates an encoding result object with a signed or encrypted message, or errors if the message encoder fails to encode the message.
- [var encodedMessage: MEEncodedOutgoingMessage?](memessageencodingresult/encodedmessage.md)
  A signed or encrypted message, if the message security handler needs to encode the message.
- [var encryptionError: (any Error)?](memessageencodingresult/encryptionerror.md)
  An error that occurred while the message encoder encrypted the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencodingresult/signingerror)*