# encryptionError

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

An error that occurred while the message encoder encrypted the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var encryptionError: (any Error)? { get }
```

*Mac Catalyst*

```objc
@property (nonatomic, copy, readonly, nullable) NSError * encryptionError;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSError * encryptionError;
```

## See Also

### Providing an Encoding Result
- [init(encodedMessage: MEEncodedOutgoingMessage?, signingError: (any Error)?, encryptionError: (any Error)?)](./init%28encodedmessage,signingerror,encryptionerror%29.md)
  Creates an encoding result object with a signed or encrypted message, or errors if the message encoder fails to encode the message.
- [var encodedMessage: MEEncodedOutgoingMessage?](./encodedmessage.md)
  A signed or encrypted message, if the message security handler needs to encode the message.
- [var signingError: (any Error)?](./signingerror.md)
  An error that occurred while the message encoder signed the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencodingresult/encryptionerror)*