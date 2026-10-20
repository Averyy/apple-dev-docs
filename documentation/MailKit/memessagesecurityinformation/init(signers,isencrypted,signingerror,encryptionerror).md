# init(signers:isEncrypted:signingError:encryptionError:)

**Framework**: MailKit  
**Kind**: init  
**Role**: Initializer

Creates a message security information object that indicates if a message is encrypted, who signed it, or if an error occurred when decoding the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?)
```

```objc
- (instancetype) initWithSigners:(NSArray<MEMessageSigner *> *) signers isEncrypted:(BOOL) isEncrypted signingError:(NSError *) signingError encryptionError:(NSError *) encryptionError;
```

## Parameters

- `signers`: An array of objects that contain information about who signed the message.
- `isEncrypted`: A Boolean value that indicates if the message is encrypted.
- `signingError`: An error that indicates the security handler couldn’t decode the message’s digital signatures.
- `encryptionError`: An error that indicates the security handler couldn’t decrypt the message.

## See Also

### Describing Message Security Attributes
- [var isEncrypted: Bool](./isencrypted.md)
  A Boolean value that indicates if the sender encrypted the message.
- [var encryptionError: (any Error)?](./encryptionerror.md)
  An error that indicates the security handler couldn’t decrypt the message.
- [var signers: [MEMessageSigner]](./signers.md)
  An array of objects that contain information about who signed the message.
- [var signingError: (any Error)?](./signingerror.md)
  An error that indicates the security handler couldn’t decode the message’s digital signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation/init(signers:isencrypted:signingerror:encryptionerror:))*