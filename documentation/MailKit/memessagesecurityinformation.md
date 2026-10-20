# MEMessageSecurityInformation

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

An object that contains details about a message’s content, such as if it’s encrypted and who digitally signed it.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageSecurityInformation
```

```objc
@interface MEMessageSecurityInformation : NSObject
```

## Topics

### Describing Message Security Attributes
- [init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?)](./memessagesecurityinformation/init%28signers,isencrypted,signingerror,encryptionerror%29.md)
  Creates a message security information object that indicates if a message is encrypted, who signed it, or if an error occurred when decoding the message.
- [var isEncrypted: Bool](./memessagesecurityinformation/isencrypted.md)
  A Boolean value that indicates if the sender encrypted the message.
- [var encryptionError: (any Error)?](./memessagesecurityinformation/encryptionerror.md)
  An error that indicates the security handler couldn’t decrypt the message.
- [var signers: [MEMessageSigner]](./memessagesecurityinformation/signers.md)
  An array of objects that contain information about who signed the message.
- [var signingError: (any Error)?](./memessagesecurityinformation/signingerror.md)
  An error that indicates the security handler couldn’t decode the message’s digital signatures.
### Initializers
- [init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?, shouldBlockRemoteContent: Bool, localizedRemoteContentBlockingReason: String?)](./memessagesecurityinformation/init%28signers,isencrypted,signingerror,encryptionerror,shouldblockremotecontent,localizedremotecontentblockingreason%29.md)
- [init?(coder: NSCoder)](./memessagesecurityinformation/init%28coder%29.md)
### Instance Properties
- [var localizedRemoteContentBlockingReason: String?](./memessagesecurityinformation/localizedremotecontentblockingreason.md)
- [var shouldBlockRemoteContent: Bool](./memessagesecurityinformation/shouldblockremotecontent.md)

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

### Decrypting Messages and Verifying Signatures
- [protocol MEMessageDecoder](./memessagedecoder.md)
  An object that decrypts messages and provides details about digital signatures.
- [class MEDecodedMessage](./medecodedmessage.md)
  An object that contains the RFC 2822 data for a message, without encryption or digital signatures.
- [class MEMessageSigner](./memessagesigner.md)
  An object that contains details about the person who signed a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation)*