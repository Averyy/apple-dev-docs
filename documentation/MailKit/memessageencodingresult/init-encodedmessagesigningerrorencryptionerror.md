# init(encodedMessage:signingError:encryptionError:)

**Framework**: MailKit  
**Kind**: init

Creates an encoding result object with a signed or encrypted message, or errors if the message encoder fails to encode the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(encodedMessage: MEEncodedOutgoingMessage?, signingError: (any Error)?, encryptionError: (any Error)?)
```

#### Discussion

If the message doesn’t require a digital signature or any encryption, specify `nil` for the message and errors.

If the message security handler does need to sign or encrypt the message, but encoding fails, specify `nil` for `encodedMessage`, and an error for one or both of the error parameters.

## Parameters

- `encodedMessage`: A signed or encrypted message.
- `signingError`: An error that occurred while signing the message.
- `encryptionError`: An error that occurred while encrypting the message.

## See Also

- [var encodedMessage: MEEncodedOutgoingMessage?](memessageencodingresult/encodedmessage.md)
  A signed or encrypted message, if the message security handler needs to encode the message.
- [var encryptionError: (any Error)?](memessageencodingresult/encryptionerror.md)
  An error that occurred while the message encoder encrypted the message.
- [var signingError: (any Error)?](memessageencodingresult/signingerror.md)
  An error that occurred while the message encoder signed the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencodingresult/init(encodedmessage:signingerror:encryptionerror:))*