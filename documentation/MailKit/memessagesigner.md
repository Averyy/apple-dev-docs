# MEMessageSigner

**Framework**: MailKit  
**Kind**: class

An object that contains details about the person who signed a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageSigner
```

## Topics

### Describing Message Signers
- [init(emailAddresses: [MEEmailAddress], signatureLabel: String, context: Data?)](memessagesigner/init(emailaddresses:signaturelabel:context:).md)
  Creates a new message signer object that contains the email addresses of the signers, a label, and context data.
- [var emailAddresses: [MEEmailAddress]](memessagesigner/emailaddresses.md)
  An array of email addresses associated with the signature.
- [var label: String](memessagesigner/label.md)
  A string that the message’s headers use to display the message signer.
- [var context: Data](memessagesigner/context.md)
  Data related to the message signature, such as the signing certificate.

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

- [protocol MEMessageDecoder](memessagedecoder.md)
  An object that decrypts messages and provides details about digital signatures.
- [class MEDecodedMessage](medecodedmessage.md)
  An object that contains the RFC 2822 data for a message, without encryption or digital signatures.
- [class MEMessageSecurityInformation](memessagesecurityinformation.md)
  An object that contains details about a message’s content, such as if it’s encrypted and who digitally signed it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesigner)*