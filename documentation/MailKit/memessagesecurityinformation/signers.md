# signers

**Framework**: MailKit  
**Kind**: property

An array of objects that contain information about who signed the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var signers: [MEMessageSigner] { get }
```

## See Also

- [init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?)](memessagesecurityinformation/init(signers:isencrypted:signingerror:encryptionerror:).md)
  Creates a message security information object that indicates if a message is encrypted, who signed it, or if an error occurred when decoding the message.
- [var isEncrypted: Bool](memessagesecurityinformation/isencrypted.md)
  A Boolean value that indicates if the sender encrypted the message.
- [var encryptionError: (any Error)?](memessagesecurityinformation/encryptionerror.md)
  An error that indicates the security handler couldn’t decrypt the message.
- [var signingError: (any Error)?](memessagesecurityinformation/signingerror.md)
  An error that indicates the security handler couldn’t decode the message’s digital signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation/signers)*