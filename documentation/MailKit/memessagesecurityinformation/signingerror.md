# signingError

**Framework**: MailKit  
**Kind**: property

An error that indicates the security handler couldn’t decode the message’s digital signatures.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var signingError: (any Error)? { get }
```

## See Also

- [init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?)](memessagesecurityinformation/init(signers:isencrypted:signingerror:encryptionerror:).md)
  Creates a message security information object that indicates if a message is encrypted, who signed it, or if an error occurred when decoding the message.
- [var isEncrypted: Bool](memessagesecurityinformation/isencrypted.md)
  A Boolean value that indicates if the sender encrypted the message.
- [var encryptionError: (any Error)?](memessagesecurityinformation/encryptionerror.md)
  An error that indicates the security handler couldn’t decrypt the message.
- [var signers: [MEMessageSigner]](memessagesecurityinformation/signers.md)
  An array of objects that contain information about who signed the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation/signingerror)*