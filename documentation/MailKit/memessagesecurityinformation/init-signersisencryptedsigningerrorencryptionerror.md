# init(signers:isEncrypted:signingError:encryptionError:)

**Framework**: MailKit  
**Kind**: init

Creates a message security information object that indicates if a message is encrypted, who signed it, or if an error occurred when decoding the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?)
```

## Parameters

- `signers`: An array of objects that contain information about who signed the message.
- `isEncrypted`: A Boolean value that indicates if the message is encrypted.
- `signingError`: An error that indicates the security handler couldn’t decode the message’s digital signatures.
- `encryptionError`: An error that indicates the security handler couldn’t decrypt the message.

## See Also

- [var isEncrypted: Bool](memessagesecurityinformation/isencrypted.md)
  A Boolean value that indicates if the sender encrypted the message.
- [var encryptionError: (any Error)?](memessagesecurityinformation/encryptionerror.md)
  An error that indicates the security handler couldn’t decrypt the message.
- [var signers: [MEMessageSigner]](memessagesecurityinformation/signers.md)
  An array of objects that contain information about who signed the message.
- [var signingError: (any Error)?](memessagesecurityinformation/signingerror.md)
  An error that indicates the security handler couldn’t decode the message’s digital signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation/init(signers:isencrypted:signingerror:encryptionerror:))*