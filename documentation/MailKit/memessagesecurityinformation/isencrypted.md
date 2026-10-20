# isEncrypted

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the sender encrypted the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var isEncrypted: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isEncrypted;
```

## See Also

### Describing Message Security Attributes
- [init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?)](./init%28signers,isencrypted,signingerror,encryptionerror%29.md)
  Creates a message security information object that indicates if a message is encrypted, who signed it, or if an error occurred when decoding the message.
- [var encryptionError: (any Error)?](./encryptionerror.md)
  An error that indicates the security handler couldn’t decrypt the message.
- [var signers: [MEMessageSigner]](./signers.md)
  An array of objects that contain information about who signed the message.
- [var signingError: (any Error)?](./signingerror.md)
  An error that indicates the security handler couldn’t decode the message’s digital signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation/isencrypted)*